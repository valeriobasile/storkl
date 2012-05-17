from django import forms
from django.forms import ModelForm, Textarea
from storklapp.models import *

def validate_new_project_name(value):
    # check if homonym project already exists
    # this should allow for different users having homonym projects,
    # now it doesn't.
    if Project.objects.filter(name=value).exists():
        raise ValidationError(u'A project with the same name already exists.')
        
class NewProjectForm(forms.Form):
    name = forms.CharField(max_length=100, label="New Project", validators=[validate_new_project_name])

class NewTaskForm(forms.Form):
    name = forms.CharField(max_length=100, label="New Task", required=False)
            
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['description']
        
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['completed']

class TaskFormOwner(ModelForm):
    users_add = forms.CharField(label="Add People", widget=Textarea(attrs={'cols': 20, 'rows': 5}), required=False)
    users_remove = forms.MultipleChoiceField(label="Remove users", widget=forms.CheckboxSelectMultiple, required=False)
    
    def __init__(self, *args, **kwargs):
        super(TaskFormOwner, self).__init__(*args, **kwargs)
        user_choices = [(user.id, user.username) for user in self.instance.users.all()]
        self.fields["users_remove"].choices=user_choices
        dep_choices = [(task.id, task.name) for task in Task.objects.filter(project=self.instance.project).exclude(pk=self.instance.id)]
        self.fields["dependencies"].choices = dep_choices
        self.fields["dependencies"].help_text=""
        
    class Meta:
        model = Task
        fields = ['completed', 'description', 'deadline', 'users_add', 'users_remove', 'dependencies']
        widgets = {'dependencies': forms.CheckboxSelectMultiple}
        


