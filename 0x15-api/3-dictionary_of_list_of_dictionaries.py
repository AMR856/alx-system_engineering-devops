#!/usr/bin/python3
"""A script that uses some things to do things"""
import json
import re
import requests
import sys
if __name__ == "__main__":
    the_url = f"https://jsonplaceholder.typicode.com/users/"
    emp_response = eval(requests.get(the_url).content.decode('utf-8'))
    emp_tasks = requests.get(f"https://jsonplaceholder.typicode.com/TODOS/",)
    emp_task_d = emp_tasks.content.decode('utf-8')
    emp_tasks_re = re.sub('false', 'False', re.sub('true', 'True', emp_task_d))
    emp_tasks_complete = eval(emp_tasks_re)
    tasks_num = len(emp_tasks_complete)
    temp_dic = {}
    json_list_employ = []
    json_list_all = []
    current_c = 1
    for task in emp_tasks_complete:
        if current_c == task['userId']:
            temp_dic = {'username': emp_response[current_c - 1]['username'],
                        'task': task['title'], 'completed': task['completed']}
            json_list_employ.append(temp_dic)
        else:
            json_list_all.append(json_list_employ)
            json_list_employ = []
            current_c = current_c + 1
    json_list_all.append(json_list_employ)
    current_c = 1
    final_dict = {}
    for item in json_list_all:
        final_dict[current_c] = item
        current_c = current_c + 1
    final_dump = json.dumps(final_dict)
    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        file.write(final_dump)
