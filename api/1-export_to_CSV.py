#!/usr/bin/python3
""" Api test script """
import csv
import requests
import sys


def get_todo_list(employee_id):
    """Gets the todo list from the employees"""

    filename = "{}.csv".format(employee_id)

    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}"
        .format(employee_id))
    employee_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))

    temp = []
    with open(filename, 'w+') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for value in employee.json():
            Username = value.get('username')
            temp.append(employee_id)
            temp.append(Username)
        for task in employee_todo.json():
            temp.extend([str(task.get("completed")), task.get('title')])
            csvwriter.writerow(temp)
            temp = temp[:-2]
    csvfile.close()

if __name__ == '__main__':
    get_todo_list(sys.argv[1])
