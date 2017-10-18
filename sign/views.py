from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
    return render(request, 'index.html')
# Create your views here.
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # response.set_cookie('user',username,3600) #浏览器添加cookie，‘user’是cookie名，‘username’是用户名，3600是cookie信息在浏览器中保存时间
            request.session['user'] = username #将session信息记录到浏览器中
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            # return HttpResponse('login fail:username and password error')
            return render(request,'index.html', {'error':'username and password error'})
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','') #读取浏览器cookie信息
    username = request.session.get('user','') #读取浏览器session信息
    return render(request, 'event_manage.html',{'user':username})
