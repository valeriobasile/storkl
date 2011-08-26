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
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pygraphviz as pgv

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
    users_add = forms.CharField(label="Add People", widget=Textarea(attrs={'cols': 40, 'rows': 10}), required=False)
    users_remove = forms.MultipleChoiceField(label="Remove users", widget=forms.CheckboxSelectMultiple, required=False)
    
    def __init__(self, *args, **kwargs):
        super(TaskFormOwner, self).__init__(*args, **kwargs)
        user_choices = [(user.id, user.username) for user in self.instance.users.all()]
        self.fields["users_remove"].choices=user_choices
        dep_choices = [(task.id, task.name) for task in Task.objects.filter(project=self.instance.project).exclude(pk=self.instance.id)]
        self.fields["dependencies"].choices = dep_choices
        
    class Meta:
        model = Task
        fields = ['description', 'deadline', 'completed', 'users_add', 'users_remove', 'dependencies']
        widgets = {'dependencies': forms.CheckboxSelectMultiple}
        
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

    # project graph
    project_graph = pgv.AGraph(strict=False,directed=True)
    project_graph.node_attr['shape']='oval'
    for task in tasks:
        project_graph.add_node(task.name)
        for dependency in task.dependencies.all():
            project_graph.add_edge(dependency.name, task.name)

    project_graph.layout(prog='dot')
    project_graph.draw('%s/project_%d.png' % (default_storage.path("graphs/projects"), project.id))

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
        default_storage.delete("graphs/projects/project_%d.png" % project_id)
        project.delete()
        
        
    return HttpResponseRedirect('/dashboard')    

@login_required()
def task(request, task_id):
    
    task = get_object_or_404(Task, pk=task_id)

    edit_authorized = request.user in task.users.all()
    owner = request.user == task.project.owner

    # processing form for edit
    if edit_authorized or owner:
        if request.method == "POST":
            if owner:
                form = TaskFormOwner(request.POST, instance=task)
                if form.is_valid():
                    task.completed = form.cleaned_data["completed"]
                    task.description = form.cleaned_data["description"]
                    task.deadline = form.cleaned_data["deadline"]
                    
                    # adding users to task
                    for user in form.cleaned_data["users_add"].split("\n"):
                        try:
                            new_user = User.objects.get(username=user)
                        except:
                            new_user = None
                        if new_user and not (new_user in task.users.all()):
                            task.users.add(new_user)
                    
                    # removing users from task
                    for user_id in form.cleaned_data["users_remove"]:
                        old_user = User.objects.get(pk=user_id)
                        task.users.remove(old_user)
                        
                    # updating dependencies
                    # debug
                    #import pdb; pdb.set_trace()        
                    task.dependencies=[]
                    for dependency in form.cleaned_data["dependencies"]:
                        if dependency and not (dependency in task.dependencies.all()):
                            task.dependencies.add(dependency)

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
