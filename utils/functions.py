import requests
import json
from operator import itemgetter
from datetime import datetime

def load_operations():
    """Получает иформацию по банковским операциям из источника"""
    operations = requests.get('https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677696419445&signature=53p_rqALxByUqE2gapbvO79cOlOy7NhzevjwTq3UhKI&downloadName=operations.json')
    all_operations = json.loads(operations.text)
    return all_operations

all_operations = load_operations()

def sorting_data(all_operations, count_operations=-5):
    """Выводит данные по последним 5(по умолчанию) исполненным операциям"""
    data_list =[]
    count = -5 if count_operations is None else count_operations
    for position in all_operations:
        if position != {} and position['state'] == 'EXECUTED':
            data_list.append(position)
    new_list = sorted(data_list, key=itemgetter('date'))
    return new_list[count:]








