#!/usr/bin/python3
"""Returns information about an employee's TODO list progress."""
import requests
import sys


def ggp_show_progress(ggp_employee_id):
    """Prints the TODO list progress of the given employee."""
    ggp_base = "https://jsonplaceholder.typicode.com"
    ggp_user = requests.get(
        "{}/users/{}".format(ggp_base, ggp_employee_id)).json()
    ggp_todos = requests.get(
        "{}/todos".format(ggp_base),
        params={"userId": ggp_employee_id}).json()
    ggp_done = [ggp_t for ggp_t in ggp_todos if ggp_t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        ggp_user.get("name"), len(ggp_done), len(ggp_todos)))
    for ggp_task in ggp_done:
        print("\t {}".format(ggp_task.get("title")))


if __name__ == "__main__":
    ggp_show_progress(int(sys.argv[1]))
