#!/usr/bin/python3
""" Api test script """
import json
import requests
import sys


def get_todo_list(employee_id):
    """Gets the todo list from the employees"""

    filename = "{}.json".format(employee_id)

    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}"
        .format(employee_id))
    employee_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))

    temp = []
    with open(filename, 'w+') as fileX:

        for value in employee.json():
            Username = value.get('username')

        for task in employee_todo.json():
            temp_dict = {"task": task.get('title'),
                "completed": task.get("completed"),
                "username": Username}
            temp.append(temp_dict)

        employee_id_dict = {employee_id: temp}
        json.dump(employee_id_dict, fileX)

if __name__ == '__main__':
    get_todo_list(sys.argv[1])
