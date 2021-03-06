Storkl
======
Simple Time ORganizing Kit ("L" is for fashion).

Storkl is a platform for project and task management, designed to be simple and inter-operable. 

Task color code:
----------------
- no deadline: grey;
- yes deadline but user not assigned to task: blue;
- deadline farther than CLOSE: green;
- deadline between CLOSE and URGENT; yellow;
- deadline closer than URGENT: red;
- past deadline: purple;

e.g. CLOSE = 3 days, URGENT = 1 day

# Glossary

- _involvement_: a **user** is involved in a **project** if she owns 
it or she has at least one **task** from the project assigned
- _ownership_: a **user** _owns_ every **project(( she creates. 
**Projects** can only have one owner.

# API

The core of Storkl's data model consists of three entities: 
**User**, **Project**, **Task**. They have statuses that change based 
on who is the (logged in) user looking at them. 

Here _STORKL_ is the base url of the Storkl installation.

## User

### GET

> _STORKL_/u/${username}

retrieves information about user ${username}

> _STORKL_/u/${username}/projects

lists projects owned by user ${username}

> _STORKL_/u/${username}/involved

lists projects in which user ${username} is involved

> _STORKL_/u/${username}/tasks

lists tasks assigned to user ${username}

### POST

> _STORKL_/u/new

creates a new user

| argument | type           | example |
| -------- | -------------- | -----  |
| username | string         | _valerio_ |
| email    | string         | _valerio@storkl.net_ |
| password | SHA-1 checksum | _229fe88b25ae8307601bf6c9c050bf02755b7e26_ |


Task
----

> _STORKL_/t/${task_id}

retrieves information about task ${task_id}

> _STORKL_/t/${task_id}/users

lists users assigned to task ${task_id}

### POST

> _STORKL_/t/new

creates a new task

| argument    | type    | example     |
| ----------- | ------- | ----------- |
| name        | string  | _buy paint_ |
| project\_id | integer | _1_         |

> _STORKL_/t/${task_id}/u/${username}/add

assign task ${task_id} to user ${username}

> _STORKL_/t/${task_id}/u/${username}/del

remove assignment of task ${task_id} from user ${username}

Project
-------

### GET

> _STORKL_/p/${project_id}

retrieves information about project ${project_id}

> _STORKL_/p/${project_id}/involved

lists users involved in pproject ${project_id}

### POST

> _STORKL_/t/new

creates a new project

