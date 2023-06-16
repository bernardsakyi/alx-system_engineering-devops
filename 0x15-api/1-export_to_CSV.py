#!/usr/bin/python3
"""
Exports the api response to a CSV file
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    filename = employee_id + ".csv"

    employee = requests.get(url + "users/" + employee_id)
    employee = employee.json()

    tasks = requests.get(url + "todos?userId=" + employee_id)
    tasks = tasks.json()

    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for item in tasks:
            writer.writerow((item.get('userId'), employee.get('username'),
                            item.get('completed'), item.get('title')))
