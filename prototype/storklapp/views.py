from storklapp.models import *
from forms import *
from utils import *

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import pygraphviz as pgv

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

            # computing colors
            task.color = task_color(task, request.user)
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
    project_graph.graph_attr['rankdir']='LR'
    project_graph.node_attr['shape']='rect'
    project_graph.node_attr['style']='filled'
    for task in tasks:
        project_graph.add_node(task.name)
        project_graph.get_node(task.name).attr["URL"]="/task/%d" % task.id        
        project_graph.get_node(task.name).attr["fillcolor"]=task_color(task, request.user)
        for dependency in task.dependencies.all():
            project_graph.add_edge(dependency.name, task.name)

    project_graph.draw('%s/project_%d.svg' % (default_storage.path("graphs/projects"), project.id), prog='dot', format='svg')
    # bug: cannot write an empty map file
    if len(tasks)>0:
        project_graph.draw('%s/maps/project_%d.html' % (settings.TEMPLATE_DIRS[0], project.id), prog='dot', format='cmap')
    else:
        open('%s/maps/project_%d.html' % (settings.TEMPLATE_DIRS[0], project.id), "w")
        
    mapfile = '%s/maps/project_%d.html' % (settings.TEMPLATE_DIRS[0], project.id)

    return render_to_response("storklapp/project.html", {'project': project, 'tasks': tasks, 'owned': owned, 'form': form, 'mapfile': mapfile}, context_instance=RequestContext(request))
    
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
        default_storage.delete("graphs/projects/project_%d.svg" % project.id)
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
                    # debug
                    #import pdb; pdb.set_trace()        
                    for user in form.cleaned_data["users_add"].split():
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
                    task.dependencies=[]
                    for dependency in form.cleaned_data["dependencies"]:
                        if dependency and not (dependency in task.dependencies.all()):
                            task.dependencies.add(dependency)

                    task.save()
                    return HttpResponseRedirect('/project/%d' % task.project.id)
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
                
    # task graph
    task_graph = pgv.AGraph(strict=False,directed=True)
    task_graph.graph_attr['rankdir']='LR'
    task_graph.node_attr['shape']='rect'
    task_graph.node_attr['style']='filled'
    task_graph.add_node(task.name)
    task_graph.get_node(task.name).attr["URL"]="/task/%d" % task.id        
    task_graph.get_node(task.name).attr["fillcolor"]=task_color(task, request.user)
    for other_task in Task.objects.all():
        if  task in other_task.dependencies.all():
            task_graph.add_node(other_task.name)
            task_graph.get_node(other_task.name).attr["URL"]="/task/%d" % other_task.id
            task_graph.get_node(other_task.name).attr["fillcolor"]=task_color(other_task, request.user)
            task_graph.add_edge(task.name, other_task.name)
    for dependency in task.dependencies.all():
        task_graph.add_node(dependency.name)
        task_graph.get_node(dependency.name).attr["URL"]="/task/%d" % dependency.id
        task_graph.get_node(dependency.name).attr["fillcolor"]=task_color(dependency, request.user)
        task_graph.add_edge(dependency.name, task.name)

    task_graph.draw('%s/task_%d_%d.svg' % (default_storage.path("graphs/tasks"), task.project.id, task.id), prog='dot', format='svg')
    task_graph.draw('%s/maps/task_%d_%d.html' % (settings.TEMPLATE_DIRS[0], task.project.id, task.id), prog='dot', format='cmap')
    
    mapfile = '%s/maps/task_%d_%d.html' % (settings.TEMPLATE_DIRS[0], task.project.id, task.id)
    
    return render_to_response("storklapp/task.html", {'task': task, 'form': form, 'owner': owner, 'mapfile': mapfile}, context_instance=RequestContext(request))

@login_required()
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    project_id = task.project.id
    
    if request.user == task.project.owner:    
        # delete task 
        default_storage.delete("graphs/tasks/task_%d_%d.svg" % (task.project.id, task.id))
        task.delete()
        
    return HttpResponseRedirect('/project/%d' % project_id)    

def view_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/?next=/dashboard')
