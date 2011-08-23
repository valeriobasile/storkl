from storklapp.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext

class NewProjectForm(forms.Form):
    name = forms.CharField(max_length=100)

@login_required(login_url='/accounts/login/')
def projects(request):
    # processing "New Project" form
   
    if request.method == "POST":
        form = NewProjectForm(request.POST)
        if form.is_valid():
            new_project = Project(name=form.cleaned_data["name"], owner=request.user.id)
            new_project.save()
            pass
    else:
        form = NewProjectForm()
    
    
    # project list
    projects = []
    tasks = Task.objects.all()
    for task in tasks:
    	if request.user in task.users.all():
    		projects.append(task.project)
    
    projects += Project.objects.filter(owner=request.user.id)
    projects = list(set(projects))
    
    return render_to_response("storklapp/projects.html", {'projects': projects, 'form': form}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def project(request, project):
	return render_to_response("storklapp/project.html", {'project': project}, context_instance=RequestContext(request))
    

def view_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/?next=/projects')
