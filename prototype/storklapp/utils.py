from storklapp.models import *
import datetime

CLOSE = 3
URGENT = 1

def task_color(task, user):
    if not user in task.users.all():
        # grey
        color = "#a0a0a0"
    else:
        if task.completed:
            # green
            color = "#90f090"
        elif task.deadline:
            delta = task.deadline - datetime.date.today() 
            if delta.days > CLOSE:
                # blue
                color = "#9090f0"
            elif delta.days > URGENT:
                # yellow
                color = "#f0f090"
            elif delta.days > -1:
                # red
                color = "#f09090"
            else:
                # purple
                color = "#f090f0"
        else:
            # grey
            color = "#a0a0a0"
    
    return color
  
