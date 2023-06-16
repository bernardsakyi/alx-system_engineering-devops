#!/usr/bin/python3
"""
Script returns nested dictionaries
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    filename = "todo_all_employees.json"

    employees = requests.get(url + "users/")
    employees = employees.json()

    employee_tasks = {}
    for employee in employees:
        employee_id = employee.get('id')
        tasks = requests.get(url + "todos?userId=" + str(employee_id))
        tasks = tasks.json()

        tasks_list = []
        for item in tasks:
            tasks_list.append(item)

        employee_tasks[employee_id] = tasks_list

    with open(filename, mode="w") as json_file:
        json.dump(employee_tasks, json_file)
