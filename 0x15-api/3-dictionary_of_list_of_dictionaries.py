#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":

    import requests
    import json

    dict = {}
    response_user = requests.get(
        "https://jsonplaceholder.typicode.com/users",
    )

    users = response_user.json()
    for user in users:
        userId = user['id']
        username = user['username']

        response_todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={'userId': userId}
        )

        tasks = [
            {
                'task': task['title'],
                'completed': task['completed'],
                'username': username
            } for task in response_todo.json()
        ]

        dict[userId] = tasks

    with open('file.json', 'w') as file:
        json.dump(dict, file)
