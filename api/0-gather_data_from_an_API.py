#!/usr/bin/python3
""" Api test script """
import requests


def get_todo_list(employee_id):
    """Gets the todo list from the employees"""
    
    #Get employee and todo list
    employee = requests.get(f"https://jsonplaceholder.typicode.com/users?id={employee_id}")
    employee_todo = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    employee_name = None
    number_tasks_done = []
    number_tasks_total = 0
    
    #Get employee name
    for value in employee.json():
        employee_name = value.get('name')
    
    #get task number and title of done tasks
    for value in employee_todo.json():
        number_tasks_total += 1
        if value.get('completed') == True:
            number_tasks_done.append(value.get('title'))

    print(f"Employee {employee_name} is done with tasks({len(number_tasks_done)}/{number_tasks_total}):")
    #display all remaining tasks here
    for i in number_tasks_done:
        print(f"   {i}")
