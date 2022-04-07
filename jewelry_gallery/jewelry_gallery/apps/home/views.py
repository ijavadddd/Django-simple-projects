from django.shortcuts import render
from django.conf import settings
from django.views import View
from .forms import RegisterForm ,LoginForm
from . import models

# Create your views here.
class home(View):
    def get(self, request):
        register_form=RegisterForm
        login_form=LoginForm
        context={
            'media':settings.MEDIA_URL,
            'register_form':register_form,
            'login_form':login_form,
        }
        if request.COOKIES.get('FirstName'):
            FirstName=request.COOKIES['FirstName']
            context['FirstName']=f'Welcome {FirstName}'
        return render(request,'home/index.html', context) 
        
    def post(self, request):
        register_form=RegisterForm
        login_form=LoginForm
        context={
            'media':settings.MEDIA_URL,
            'register_form':register_form,
            'login_form':login_form,
        }
        register=register_form(request.POST)
        if register.is_valid():
            register_data=register.cleaned_data
            user=models.User()
            user.FirstName=register_data['FirstName']
            user.PhoneNumber=register_data['PhoneNumber']
            user.Password=register_data['Password']
            user.Address=None
            user_role=models.Role.objects.get(Title='Normal')
            user.Role=user_role
            user.save()
            response=render(request,'home/index.html', context) 
            response.set_cookie(key='FirstName', value=register_data['FirstName'],max_age=1200)
            return response

            
        login=login_form(request.POST)
        users=models.User.objects.all()
        print(list(users))
        if login.is_valid():
            login_data = login.cleaned_data
            users=models.User.objects.all()
            for user in users:
                if user['PhoneNumber']==login_data['PhoneNumber']:
                    if user['password']==login_data['Password']:
                        print('salam')
                        response=render(request,'home/index.html', context) 
                        response.set_cookie(key='PhoneNumber', value=login_data['PhoneNumber'])
                        return response
                    else:
                        print('PhoneNumber or password is incorrect.')
        return render(request,'home/index.html', context) 