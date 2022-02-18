from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login, logout, authenticate
User = get_user_model()
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .form import CustomUserCreationForm, ProfileForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# Create your views here.


def registerUser(request):
    page = 'register'    
    # initials = {
    #     'username': "username",
    #     'email' : 'xyz@gmail',
    #      'password1':'000000',
    #      'password2': '000000'
        
    # }
    form =  CustomUserCreationForm()
    
    if request.method =='POST':        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active = False
            user.save()
            messages.success(request, 'Please Check the mail and confirm your account')
            current_site = get_current_site(request)
            mail_subject='Activate Your Account'
            message= render_to_string('send_mail.html', {
                'user':user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail = user.email
            email = EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            return redirect('home')
        else:
          messages.success(request, 'An error has occurred during registration')

    context = {'page':page, 'form':form}
    return render(request, 'login_register.html', context)
        
def activate(request, uidb64, token):
    try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
            user=None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has created!')
        login(request, user)
        return redirect('edit-account')
    else:
        messages.warning(request, "Activation link invalid!")
        

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    cv = profile.resumemodel_set.all()
    context = {'profile':profile, 'cv':cv}
    
    return render(request, 'account.html',context)

def loginUser(request):
    
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    form = ProfileForm()
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)  
        except:
            messages.error(request,'User name does not exist!')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Username OR password is incorrect')
              
    context = {'form':form, 'page':page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'Users was logged out!')
    return redirect('home')

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    try:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form = form.save(commit=False)
                form.name = form.first_name+" "+ form.last_name
                form.save()
                return redirect('account')
    except:
        messages.error(request, 'Please Fill Up All Required Field Correctly')
        return redirect('edit-account')
    context = {'form':form}
    return render(request, 'profile-form.html',context)