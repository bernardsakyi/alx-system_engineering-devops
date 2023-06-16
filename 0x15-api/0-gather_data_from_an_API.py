#!/usr/bin/python3
"""  Gather data from an API using request """


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    employee = requests.get(url + "users/" + employee_id)
    employee = employee.json()

    tasks = requests.get(url + "todos?userId=" + employee_id)
    tasks = tasks.json()

    tasks_done_list = []
    for item in tasks:
        if item.get('completed') is True:
            tasks_done_list.append(item)

    tasks_done = len(tasks_done_list)
    tasks_total = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), tasks_done, tasks_total))
    for item in tasks_done_list:
        print("\t {}".format(item.get('title')))
