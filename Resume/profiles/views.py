from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login, logout, authenticate
User = get_user_model()
from django.contrib import messages
from .form import CustomUserCreationForm, ProfileForm

# Create your views here.


def registerUser(request):
    page = 'register'    
    form =  CustomUserCreationForm()
    
    if request.method =='POST':        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User Account was created!')
            login(request, user)
            return redirect('edit-account')
        else:
          messages.success(request, 'An error has occurred during registration')

            
    context = {'page':page, 'form':form}
    return render(request, 'login_register.html', context)

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