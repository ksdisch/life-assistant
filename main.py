from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

# allows user to dynamically create lists and corresponding forms 
def new_list_input_form_generator(details):
    class ListInputForm(FlaskForm):
        # details will be the keys of the dictionary that is created when the user creates a new list
        for detail in details:
            detail_input = StringField(f'{detail}: ')
        submit = SubmitField('Submit')

    return ListInputForm


app = Flask(__name__)

# this dict will store all of the lists that the user creates. These lists could be tasks, goals, ideas, hobbies, habits to build, habits to break, interesting topics, interesting activities, videos to watch, movies to watch, shows to watch, etc.
user_lists_dict = {
# Initialize empty lists for tasks and completed tasks in the user lists dictionary
# Each task will be a dictionary with the task as well as details about it
'tasks': [
    {"task": "do laundry", "priority": "high", "time commitment": "low"}, 
    {"task": "fold laundry", "priority": "medium", "time commitment": "medium"}, 
    ],
'completed_tasks': [
    {"task": "workout", "priority": "low", "time commitment": "high"},
    ]
}
# append to this as new lists are created
# user_lists = [tasks]

# for user to select from the lists that they have created when adding tasks
user_list_labels = [key for key in user_lists_dict]
class ListForm(FlaskForm):
    # where the new task will be added -> should trigger the corresponding form to be brought up
    list_choice = SelectField('List to add item to', choices=[(list_name, list_name.title()) for list_name in user_list_labels])
    
tasks_form = new_list_input_form_generator([key for key in user_lists_dict['tasks']])

# Define routes

# index route - renders an HTML template displaying the tasks and completed tasks lists
@app.route('/')
def index():
    return render_template('index.html', tasks=user_lists_dict['tasks'], completed_tasks=user_lists_dict['completed_tasks'], task_list_form=tasks_form)



# add_task route - adds a task to the appropriate list based on the list_name parameter
@app.route('/add_task', methods=['POST'])
def add_task():
    # get the list that they are trying to add the task to
    list_form = ListForm()
    list_input = 

    # task = request.form['task']
    # list_name = request.form['list_name']
    
    # # Add task to appropriate list
    # if list_name == 'Completed Tasks':
    #     completed_tasks.append(task)
    # else:
    #     tasks.append(task)
    # flask function that reroutes you to a given page (in this case the home page) 
    return redirect('/')


# complete_task route - moves task from given tasks list to completed tasks list
@app.route('/complete_task', methods=['POST'])
def complete_task():
    task = request.form['task']
    
    # Move task from tasks to completed_tasks
    if task in tasks:
        tasks.remove(task)
        completed_tasks.append(task)
        
    return redirect('/')

if __name__ == '__main__':
    app.run()
