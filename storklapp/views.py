from storklapp.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea

def validate_new_project_name(value):
    # check if homonym project already exists
    # this should allow for different users having homonym projects,
    # now it doesn't.
    if Project.objects.filter(name=value).exists():
        raise ValidationError(u'A project with the same name already exists.')
        
class NewProjectForm(forms.Form):
    name = forms.CharField(max_length=100, label="New Project", validators=[validate_new_project_name])

class NewTaskForm(forms.Form):
    name = forms.CharField(max_length=100, label="New Task")

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['description']
        
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['completed']

class TaskFormOwner(ModelForm):
    users = forms.CharField(label="Add People", widget=Textarea(attrs={'cols': 40, 'rows': 10}))
    
    class Meta:
        model = Task
        fields = ['description', 'deadline', 'completed']

        
@login_required()
def dashboard(request):
    # processing "New Project" form
    if request.method == "POST":
        form = NewProjectForm(request.POST)        
        if form.is_valid():
            new_project = Project(name=form.cleaned_data["name"], owner=request.user)
            new_project.save()
            return HttpResponseRedirect('/project/%d' % new_project.id)
    else:
        form = NewProjectForm()
    
    # project list
    projects = []
    tasks = []
    for task in Task.objects.all():
        if request.user in task.users.all():
            projects.append(task.project)
            tasks.append(task)
                    
    projects += Project.objects.filter(owner=request.user.id)
    projects = list(set(projects))
    
    return render_to_response("storklapp/dashboard.html", {'projects': projects, 'tasks': tasks, 'form': form}, context_instance=RequestContext(request))

@login_required()
def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
     # processing "New Task" form
    if request.method == "POST":
        form = NewTaskForm(request.POST)        
        if form.is_valid():
            new_task = Task(name=form.cleaned_data["name"], project=project)
            new_task.save()
            return HttpResponseRedirect('/task/%d' % new_task.id)
    else:
        form = NewTaskForm()
    
    if request.user == project.owner:
        owned = True
    else:
        owned = False
       
    # task list
    tasks = Task.objects.filter(project=project)

    return render_to_response("storklapp/project.html", {'project': project, 'tasks': tasks, 'owned': owned, 'form': form}, context_instance=RequestContext(request))
    
@login_required()
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    # processing "Project" form
    if request.method == "POST":
        form = ProjectForm(request.POST)        
        if form.is_valid():
            project.description = form.cleaned_data["description"]
            project.save()
            return HttpResponseRedirect('/project/%d' % project.id)
    else:
        form = ProjectForm(instance=project)
    
    # task list
    tasks = Task.objects.filter(project=project)

    return render_to_response("storklapp/edit_project.html", {'project': project, 'tasks': tasks, 'form': form}, context_instance=RequestContext(request))

@login_required()
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.user == project.owner:
        # delete project
        project.delete()
        
    return HttpResponseRedirect('/dashboard')    

@login_required()
def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    edit_authorized = request.user in task.users.all()
    owner = request.user == task.project.owner

    # processing "Task" form
    if edit_authorized or owner:
        if request.method == "POST":
            if owner:
                form = TaskFormOwner(request.POST)
                if form.is_valid():
                    task.completed = form.cleaned_data["completed"]
                    task.description = form.cleaned_data["description"]
                    task.deadline = form.cleaned_data["deadline"]
                    
                    for user in form.cleaned_data["users"].split("\n"):
                        try:
                            new_user = User.objects.get(username=user)
                        except:
                            new_user = None
                            
                        if new_user and not (new_user in task.users.all()):
                            task.users.add(new_user)
                    
                    task.save()
                    return HttpResponseRedirect('/task/%d' % task.id)
            else:
                form = TaskForm(request.POST)
                if form.is_valid():
                    task.completed = form.cleaned_data["completed"]
                    task.save()
                    return HttpResponseRedirect('/task/%d' % task.id)
        else:
            if owner:
                form = TaskFormOwner(instance=task)
            else:
                form = TaskForm(instance=task)
    else:
        form = None
        
    return render_to_response("storklapp/task.html", {'task': task, 'form': form}, context_instance=RequestContext(request))
    
def view_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/?next=/dashboard')
