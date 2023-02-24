from django.shortcuts import render


def check_authenticate(myfunc):
    def inner(request):
        if request.user.is_authenticated:
            resp=render(request,'product/main.html')
            return resp
        else:
            return myfunc(request) 
    return inner