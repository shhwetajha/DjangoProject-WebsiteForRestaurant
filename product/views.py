from django.shortcuts import render
from .forms import BookingForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from  django.contrib.auth.decorators import login_required
from .decorator import check_authenticate

# Create your views here.
def view_main(request):
    resp=render(request,'product/main.html')
    return resp
    

def view_home(request):
    resp=render(request,'product/home.html')
    return resp
    
def view_about(request):
    resp=render(request,'product/about.html')
    return resp
    

def view_blogs(request):
    resp=render(request,'product/blogs.html')
    return resp

@check_authenticate
def view_registeration(request):
    if request.method=='GET':
        frm_unbound=UserCreationForm()
        dict={"forms":frm_unbound}
        resp=render(request,'product/register.html',context=dict)
        return resp
    elif request.method=='POST':
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=render(request,'product/login.html')
            return resp

@check_authenticate
def view_login(request):
    if request.method=='GET':
        resp=render(request,'product/login.html')
        return resp
    elif request.method=='POST':
        u_name=request.POST.get('t1','N.A')
        u_password=request.POST.get('p1','N.A')
        u=authenticate(request=request,username=u_name,password=u_password)
        if u is not None:
            login(request=request,user=u)
            resp=render(request,'product/main.html')
            return resp
        else:
            resp=render(request,'product/login.html')
            return resp


def view_logout(request):
    logout(request=request)
    resp=render(request,'product/login.html')
    return resp


@login_required(login_url='login')
def view_book_table(request):
    if request.method=='GET':
        frm_bound=BookingForm()
        dict={"forms":frm_bound}
        resp=render(request,'product/book_table.html',context=dict)
        return resp
    elif request.method=='POST':
        frm_unbound=BookingForm(request.POST)
        if frm_unbound.is_valid():
            frm_unbound.save()
            resp=HttpResponse('<h1>Booking done successfully!!!</h1>')
            return resp
        else:
            dict={"forms":frm_unbound}
            resp=render(request,'product/book_table.html')
            return resp
    
def view_contactus(request):
    resp=render(request,'product/contactus.html')
    return resp
    
def view_gallery(request):
    resp=render(request,'product/gallery.html')
    return resp
    
def view_reviews(request):
    resp=render(request,'product/reviews.html')
    return resp

def view_components(request):
    resp=render(request,'product/components.html')
    return resp



       