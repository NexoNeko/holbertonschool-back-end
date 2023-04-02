#!/usr/bin/python3
""" Api test script """
import requests
import sys


def get_todo_list(employee_id):
    """Gets the todo list from the employees"""
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(employee_id))
    employee_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))

    employee_name = None
    number_tasks_done = []
    number_tasks_total = 0

    for value in employee.json():
        employee_name = value.get('name')

    for value in employee_todo.json():
        number_tasks_total += 1
        if value.get('completed'):
            number_tasks_done.append(value.get('title'))

    print("Employee {} is done with tasks({}/{}):".format
        (employee_name, len(number_tasks_done), number_tasks_total))

    for i in number_tasks_done:
        print("{} {}".format('\t', i))


if __name__ == '__main__':
    get_todo_list(sys.argv[1])