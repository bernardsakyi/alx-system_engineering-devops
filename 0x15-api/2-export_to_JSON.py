#!/usr/bin/python3
"""
Export api response to Json
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    filename = employee_id + ".json"

    employee = requests.get(url + "users/" + employee_id)
    employee = employee.json()

    tasks = requests.get(url + "todos?userId=" + employee_id)
    tasks = tasks.json()

    tasks_list = []
    for item in tasks:
        tasks_list.append(item)

    employee_tasks = {}
    employee_tasks[employee_id] = tasks_list

    with open(filename, mode="w") as json_file:
        json.dump(employee_tasks, json_file)
