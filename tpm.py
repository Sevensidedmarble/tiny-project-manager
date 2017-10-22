#!/usr/bin/python

# Attention reader!
# If you're reading this source file and want to know basic usage information, refer to the help_text string
# below, or run this script with no arguments.

help_text = """\
Usage: tpm [OPTIONS]
    help                              Display this message.
    name [NAME]                       Name your project.
    start, s, begin                   Begin tracking general time
    start [FEATURE]                   Begin tracking time on a feature.
    [feature, features, f]            Display a list of features and their status.
    feature [add, a] [FEATURE]        Add a new feature.
    [todo, todos, tasks, task, t]     List tasks that need to be done.
    todo [add, a]                     Add a task.
    
Any of the above aliases (such as 'f' for 'feature') can be substituted with their related
commands, such as using "tpm t a 'Do a thing tomorrow'" instead of "tpm task add 'Do a thing tomorrow'"
You can shorten them further by using flag syntax, such as 'tpm -ta' for adding a task.
"""

import sys
from datetime import datetime, timedelta

global name; name = None
global features; features = []
global log; log = []
global working_since; working_since = None
global working_on; working_on = None
global todo; todo = []

def add_feature(name, description):
    features += {'name': name, 'description': description}

def add_task(name, description=None):
    todo += {'name': name, 'description': description}

def set_name(new_name):
    name = new_name

def start(feature=None):
    # check if we're currently working.
    if working_since is not None:
        # if a projects already started, see if we started a feature or not.
        if working_on is None:
            print("Already tracking time! Type 'tpm stop' to log and end the current session, or 'tpm delete' to                        stop the current session without logging it.")
        else: # if a feature is started instead, let the user know.
            print("Already working on feature: " + working_on['name'])
    else: # there is no current time tracking, so start doing so.
        if feature is None:
            working_since = datetime.now()
            print("Starting time tracking.")
        else:
            working_since = datetime.now()
            working_on = feature
            print("Starting time tracking on feature: " + working_on['name'])

def display_help():
    print(help_text)
    sys.exit()

def main():
    first_arg = get_arg(1)
    second_arg = get_arg(2)
    second_arg = get_arg(3)

    if first_arg is None:
        display_help()
    elif first_arg.lower() in ['help', 'h']:
        display_help()
    elif first_arg.lower() in ['name']:
        parse_name_command(second_arg)
    elif first_arg.lower() in ['start', 's', 'begin']:
        parse_todo_command()
    elif first_arg.lower() in ['todo', 'todos', 't', 'task', 'tasks']:
        parse_todo_command()
    elif first_arg.lower() in ['features', 'feature', 'f']:
        parse_features_command()
    else:
        display_help()

def parse_name_command(argument):
    if argument is None:
        print("""\
        Usage: tpm name "[PROJECT NAME]"
        """)
    else:
        set_name(argument)

def parse_features_command():
    pass

def parse_todo_command():
    pass

def get_arg(index):
    try:
        return sys.argv[index]
    except IndexError:
        return None

if __name__ == "__main__":
    main()