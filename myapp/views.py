from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,Addrecordform
from .models import Data
# Create your views here.
def home(request):
    records=Data.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been Logged In')
            return redirect('home')
        else:
            messages.success(request,'There was an error')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})




def logout_user(request):
    logout(request)
    messages.success(request,"You Have been Logged out")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.changed_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You have been Logged In')
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Data.objects.get(id=pk)
        return render(request,'records.html',{'customer_record':customer_record})
    else:
        messages.success(request,'You must be Logged In')
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Data.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,'Record has been deleted')
        return redirect('home')
    else:
        messages.success(request,'You must be Logged In')
        return redirect('home')
    
def addrecord(request):
    form=Addrecordform(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                addrecord=form.save()
                messages.success(request,'Record Saved')
                return redirect('home')  
        
        return render(request,'addrecord.html',{'form':form})
    else:
        messages.success(request,'You must be Logged In')
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Data.objects.get(id=pk)
        form=Addrecordform(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated')
            return redirect('home')  
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,'You must be Logged In')
        return redirect('home')
