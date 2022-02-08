from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect

from . form import Form
from .models import ResumeModel

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def delete_cv(request, pk):
    cv = ResumeModel.objects.get(id=pk)
    cv.delete()
    return redirect('account')

@login_required(login_url='login')
def cv_creation(request):
    profile = request.user.profile
    form = Form(instance = profile)
    
    context = {'form':form}
        
    if request.method == 'POST':
        cv = Form(request.POST, request.FILES)
        if cv.is_valid():
            cv = cv.save(commit=False)
            cv.profiles = profile
            cv.save()
            resume = profile.resumemodel_set.all()
            resume = (resume[len(resume)-1])
            return HttpResponseRedirect(reverse('cv_view', args=(resume.id,)))
        
    return render(request, 'main.html', context)

def cv_view(request, pk):
    resume_cv = ResumeModel.objects.get(id=pk)
    context = {'resume_cv':resume_cv}
    
    return render(request, 'cv_templates.html', context)
