from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from django.shortcuts import render, redirect

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def register(request):
    if(request.method == 'POST'):

        username = request.POST['uname']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        email = request.POST['email']

        if(password1==password2):

            if(User.objects.filter(email=email).exists()):

                messages.info(request, 'email is already used')
                return render(request, 'register.html')

            if(User.objects.filter(username=username).exists()):

                messages.info(request, 'User name is already used')
                return render(request, 'register.html')

            user = User.objects.create_user(username=username, password = password1, email = email)
            user.save()

            return redirect('login')
        
        else:
            messages.info(request, 'password confirm failed')
    
            return render(request, 'register.html')
    
    else:
        return render(request, 'register.html')


def login(request):
    if(request.method == 'POST'):
        
        username = str(request.POST['uname'])
        password = str(request.POST['pass'])

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #This will return to original url 
            return redirect('/')
        
        else:
            messages.info(request, 'credentials incorrect')
            return redirect('login')


    else:
        return render(request, 'login.html')



def logout(request):

    auth.logout(request)
    return redirect('/')