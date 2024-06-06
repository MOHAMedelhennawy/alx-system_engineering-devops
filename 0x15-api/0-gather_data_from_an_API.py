#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    response_user = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={'id': userId}
    )

    username = response_user.json()[0]['name']
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={'userId': userId}
    )

    todos_list = response_todo.json()
    done_tasks = [task for task in todos_list if task['completed'] is True]
    print("Employee {} is done with tasks({}/{}):"
        .format(username, len(done_tasks), len(todos_list)))
    for tasks in done_tasks:
        print('\t', tasks['title'])