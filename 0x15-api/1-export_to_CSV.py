#!/usr/bin/python3
"""A script that uses some things to do things"""
import csv
import re
import requests
import sys
if __name__ == "__main__":
    user_num = str(sys.argv[1])
    the_url = f"https://jsonplaceholder.typicode.com/users/{user_num}"
    emp_response = eval(requests.get(the_url).content.decode('utf-8'))
    emp_tasks = requests.get(f"https://jsonplaceholder.typicode.com/TODOS/",
                             params={'userId': f'{user_num}'})
    emp_task_d = emp_tasks.content.decode('utf-8')
    emp_tasks_re = re.sub('false', 'False', re.sub('true', 'True', emp_task_d))
    emp_tasks_complete = eval(emp_tasks_re)
    tasks_num = len(emp_tasks_complete)
    completed_tasks_num = 0
    completed_tasks_list = []
    for task in emp_tasks_complete:
        if task['completed'] is True:
            completed_tasks_num = completed_tasks_num + 1
            completed_tasks_list.append(task)
    with open(f'{user_num}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in emp_tasks_complete:
            writer.writerow([str([task['userId']]).strip('[]'),
                            emp_response['username'],
                            str(task['completed']), task['title']])
