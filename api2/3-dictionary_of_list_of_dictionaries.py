#!/usr/bin/python3
"""Exports the TODO list data of all employees to a JSON file."""
import json
import requests
from collections import OrderedDict


def ggp_export_all():
    """Writes all tasks of all employees to todo_all_employees.json."""
    ggp_base = "https://jsonplaceholder.typicode.com"
    ggp_users = requests.get("{}/users".format(ggp_base)).json()
    ggp_todos = requests.get("{}/todos".format(ggp_base)).json()

    ggp_result = OrderedDict()
    for ggp_user in ggp_users:
        ggp_id = ggp_user.get("id")
        ggp_tasks = []
        for ggp_task in ggp_todos:
            if ggp_task.get("userId") == ggp_id:
                ggp_item = OrderedDict()
                ggp_item["username"] = ggp_user.get("username")
                ggp_item["task"] = ggp_task.get("title")
                ggp_item["completed"] = ggp_task.get("completed")
                ggp_tasks.append(ggp_item)
        ggp_result[str(ggp_id)] = ggp_tasks

    with open("todo_all_employees.json", "w") as ggp_file:
        json.dump(ggp_result, ggp_file)


if __name__ == "__main__":
    ggp_export_all()
