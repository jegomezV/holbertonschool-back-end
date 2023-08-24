#!/usr/bin/python3
"""
-------------------------------------------------------------------------------
MODULE NAME:
-------------------------------------------------------------------------------
    0-gather_data_from_an_API
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TO DO list progress.
    REST API: https://jsonplaceholder.typicode.com/
-------------------------------------------------------------------------------
REQUERIMENTS:
-------------------------------------------------------------------------------
    -You must use urllib or requests module
    -The script must accept an integer as a parameter, which is the employee ID
    -The script must display on the standard output the employee TO DO list pro
     gress in this exact format:
    -First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS
     /TOTAL_NUMBER_OF_TASKS):
    -EMPLOYEE_NAME: name of the employee
    -NUMBER_OF_DONE_TASKS: number of completed tasks
    -TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of complete
     d and non-completed tasks
    -Second and N next lines display the title of completed tasks: TASK_TITLE (
     with 1 tabulation and 1 space before the TASK_TITLE)
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    -requests: for obtain the data that we need from the API
    -argv: to obtain the id of the user to found the information
-------------------------------------------------------------------------------
STATUS CODE FOR REQUESTS
-------------------------------------------------------------------------------
    -200 OK: This status code indicates that the request was successful.
    -201 Created: New resource has been successfully created.
    -204 No Content: There is no content to send back in the response.
    -400 Bad Request: Request is malformed or contains invalid parameters.
    -401 Unauthorized: Request lacks valid authentication credentials.
    -403 Forbidden: Similar to 401, but, even if authentication is provided.
    -404 Not Found: The server could not find the requested resource.
    -405 Method Not Allowed: The requested HTTP method is not supported.
    -500 Internal Server Error: This is a generic server error message.
    -502 Bad Gateway: Server acting as a gateway or proxy received.
    -503 Service Unavailable: Server is temporal unable to handle the request.
    -504 Gateway Timeout: Similar to 502, Server acting as a gateway or proxy
            did not receive a timely response from an upstream server.
"""
import requests
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]
    response = requests.get("{}users/{}/todos".format(API_URL, user_id),
                            params={"_expand": "user"})

    if response.status_code == 200:
        data = response.json()
        name = data[0]["user"]["name"]
        task_done = [task for task in data if task["completed"]]

        print("Employee {} is done with tasks({}/{}):".format(
            name, len(task_done), len(data)))
        for task in task_done:
            print("\t {}".format(task["title"]))

    else:
        print("Error: {}".format(response.status_code))
