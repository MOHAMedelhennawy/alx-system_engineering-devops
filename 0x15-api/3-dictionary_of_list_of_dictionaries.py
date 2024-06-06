#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":

    import requests
    import json
    import sys


    response_user = requests.get(
        "https://jsonplaceholder.typicode.com/users",
    )

    all_users = response_user.json()
    for user in all_users:
        userId = response_user.json()[0]['id']
        username = response_user.json()[0]['name']
        response_todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
        )

        todos_list = response_todo.json()
        tasks = [
            {
                'task': task['title'],
                'completed': task['completed'],
                'username': username
            } for task in todos_list
            ]

        user = {}
        user[userId] = tasks
        filename = '{}.json'.format(userId)
        with open('file.json', 'w') as file:
            json.dump(user, file)
