#!/usr/bin/python3
"""Exports an employee's TODO list data to a CSV file."""
import csv
import requests
import sys


def ggp_export_csv(ggp_employee_id):
    """Writes all tasks of the given employee to USER_ID.csv."""
    ggp_base = "https://jsonplaceholder.typicode.com"
    ggp_user = requests.get(
        "{}/users/{}".format(ggp_base, ggp_employee_id)).json()
    ggp_todos = requests.get(
        "{}/todos".format(ggp_base),
        params={"userId": ggp_employee_id}).json()

    ggp_name = ggp_user.get("username")
    ggp_filename = "{}.csv".format(ggp_employee_id)
    with open(ggp_filename, "w", newline="") as ggp_file:
        ggp_writer = csv.writer(ggp_file, quoting=csv.QUOTE_ALL)
        for ggp_task in ggp_todos:
            ggp_writer.writerow([ggp_employee_id,
                                 ggp_name,
                                 ggp_task.get("completed"),
                                 ggp_task.get("title")])


if __name__ == "__main__":
    ggp_export_csv(int(sys.argv[1]))
