#!/usr/bin/python3
"""A script that uses some things to do things"""
import re
import requests
import sys
import json
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
    temp_dic = {}
    json_list = []
    for task in emp_tasks_complete:
        temp_dic = {"task": task['title'], 'completed': task['completed'], 'username': emp_response['username']}
        json_list.append((temp_dic))
    final_dump = json.dumps({user_num : json_list})
    with open(f'{user_num}.json', 'w', encoding='utf-8') as file:
        file.write(final_dump)
