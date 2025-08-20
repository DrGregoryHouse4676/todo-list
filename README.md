# Django Todo List

## Task

You should have such models:

Task - todo list is consist of tasks. Each task should have fields for:
content - describes what you should do.
datetime, when a task was created
optional deadline datetime if a task should be done until some datetime
the boolean field that marks if the task is done or not
tags that are relevant for this task
Tag - a tag symbolizes the theme of the task and consists only of a name.
A task can have multiple tags and a tag can be in multiple tasks.

Create the home page. The home page is accessed by 127.0.0.1:8000/, where you should have:

Sidebar with the links to:
Home page
Tag list page the sidebar should be on all pages.
Todo list which is a list of tasks.
Tasks should be ordered from not done to done and from newest to oldest
All task information should be displayed.
There should be a button to add a new task.
For each task add links for updating and deletion.
Also, add a button Complete if a task is not done and Undo if a task is done, this button changes the status of the task to the opposite and redirects to this page


# Launching
#### python -m venv venv
#### Mac: source venv/bin/activate 
#### Windows: venv\Scripts\activate
#### pip install -r requirements.txt
#### python manage.py migrate
#### python manage.py runserver

