#!/usr/bin/python3
"""Exports an employee's TODO list data to a JSON file."""
import json
import requests
import sys
from collections import OrderedDict


def ggp_export_json(ggp_employee_id):
    """Writes all tasks of the given employee to USER_ID.json."""
    ggp_base = "https://jsonplaceholder.typicode.com"
    ggp_user = requests.get(
        "{}/users/{}".format(ggp_base, ggp_employee_id)).json()
    ggp_todos = requests.get(
        "{}/todos".format(ggp_base),
        params={"userId": ggp_employee_id}).json()

    ggp_name = ggp_user.get("username")
    ggp_tasks = []
    for ggp_task in ggp_todos:
        ggp_item = OrderedDict()
        ggp_item["task"] = ggp_task.get("title")
        ggp_item["completed"] = ggp_task.get("completed")
        ggp_item["username"] = ggp_name
        ggp_tasks.append(ggp_item)

    ggp_filename = "{}.json".format(ggp_employee_id)
    with open(ggp_filename, "w") as ggp_file:
        json.dump({str(ggp_employee_id): ggp_tasks}, ggp_file)


if __name__ == "__main__":
    ggp_export_json(int(sys.argv[1]))
