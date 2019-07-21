from django.shortcuts import render
from .models import regandlogindata
from .forms import regform,loginform
from django.http.response import HttpResponse
def indexview(request):
    return render(request,'index.html')
def regview(request):
    if request.method=="POST":
        rform=regform(request.POST)
        if rform.is_valid():
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            location=request.POST.get('location')
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            data=regandlogindata(firstname=firstname,lastname=lastname,location=location,username=username,password=password,email=email,mobile=mobile)
            data.save()
            rform = regform()
            return render(request, 'reg.html', {'rform': rform})

        else:
            return HttpResponse("sorry Invalid data")
    else:
        rform=regform()
        return render(request,'reg.html',{'rform':rform})
def loginview(request):
    if request.method=="POST":
        lform=loginform(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            uname=regandlogindata.objects.filter(username=username)
            pwd=regandlogindata.objects.filter(password=password)
            if uname and pwd:
                return render(request,'dhamodar.html')


            else:
                return HttpResponse("Login failed")



        else:
            return HttpResponse("Invalid data")
    else:
        lform=loginform()
        return render(request,'login.html',{'lform':lform})










