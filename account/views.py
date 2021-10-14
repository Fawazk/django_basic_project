from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.sessions.models import Session
from . models import ex,emp,cards
# Create your views here.

datas={'ex':ex,'emp':emp,'cards':cards}
@never_cache
def home(request):
    if request.session.has_key('key'):
        return render(request,'index.html',datas)
    else:
        return redirect('login')
    
@never_cache  
def login(request):
    if request.session.has_key('key'):
        # cookie = Session.objects.get(session_key=request.COOKIES.get('key'))
        # data = cookie.get_decoded()
        # if data.get('key') != request.session['key']:
            return redirect('home')
    else:
        if request.method=='POST': 
            username = request.POST['username']
            password = request.POST['password']
            if username=='admin' and password=='1234':
                request.session['key']='value'
        
                return redirect('home')
            else:
                messages.error(request,'invalid username or password')
                return redirect('home')
        else:
            return render(request,'login.html')

@never_cache  
def logout(request):
    if request.session.has_key('key'):
        request.session.flush()
        return redirect('login')
    
    
