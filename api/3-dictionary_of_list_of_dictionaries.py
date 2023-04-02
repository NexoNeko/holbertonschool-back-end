#!/usr/bin/python3
""" Api test script """
import json
import requests
import sys


def get_todo_list():
    """Gets the todo list from the employees"""

    filename = "todo_all_employees.json"

    employee_id = 1
    employee_id_dict = {}
    temp = []
    while True:
        employee = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}"
            .format(employee_id))
        employee_todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(employee_id))

        if employee.json() == []:
            break

        for value in employee.json():
            Username = value.get('username')
        for element in employee_todo.json():
            temp_dict = {
                        "username": Username,
                        "task": element.get('title'),
                        "completed": element.get("completed")}
            hold = temp_dict.copy()
            temp.append(hold)

        newlist = temp.copy()
        employee_id_dict.update({employee_id: newlist})
        temp.clear()
        temp_dict.clear()
        employee_id += 1

    with open(filename, 'w+') as fileX:
        json.dump(employee_id_dict, fileX)

if __name__ == '__main__':
    get_todo_list()
