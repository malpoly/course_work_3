import requests
import json
from datetime import datetime

def load_operations():
    """Получает иформацию по банковским операциям из какого-то источника"""
    operations = requests.get('https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677696419445&signature=53p_rqALxByUqE2gapbvO79cOlOy7NhzevjwTq3UhKI&downloadName=operations.json')
    all_operations = json.loads(operations.text)
    return all_operations

all_operations = load_operations()

def sorting_data(all_operations, count_operations=-5):
    """Выводит списком все даты, сортирует их и возвращает пять последних операций"""
    data_list =[]
    count = -5 if count_operations is None else count_operations
    for position in all_operations:
        if position != {}:
            data_list.append(position['date'])
    data_list.sort()
    return data_list[count:]








