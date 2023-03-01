import requests
import json
from operator import itemgetter
from datetime import datetime

def load_operations():
    """Получает иформацию по банковским операциям из источника"""
    operations = requests.get('https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677696419445&signature=53p_rqALxByUqE2gapbvO79cOlOy7NhzevjwTq3UhKI&downloadName=operations.json')
    all_operations = json.loads(operations.text)
    return all_operations


def sorting_data(all_operations, count_operations=-5):
    """Выводит данные по последним 5(по умолчанию) исполненным операциям"""
    data_list =[]
    count = -5 if count_operations is None else count_operations
    for position in all_operations:
        if position != {} and position['state'] == 'EXECUTED':
            data_list.append(position)
    new_list = sorted(data_list, key=itemgetter('date'))
    return new_list[count:]


def change_data(new_list):
    """Меняет формат данных для вывода даты"""
    for i in new_list:
        date_new = datetime.fromisoformat(i['date'])
        date_formatted = date_new.strftime("%d.%m.%Y")  # День Месяц Год
        i['date'] = date_formatted
    return new_list

def preparation_accounts(new_list):
    """Меняет формат вывода счетов"""
    for i in new_list:
        i['to'] = "Счет **" + i['to'][-4:]
        if i.get(('from')) != None:
            if "Maestro" in i['from']:
                i['from'] = "Maestro " + i['from'][8:12] + " **** **** " + i['from'][-4:]
            elif "Visa" in i['from']:
                i['from'] = "Visa Classic " + i['from'][12:17] + " **** **** " + i['from'][-4:]
            elif "Счет" in i['from']:
                i['from'] = "Счет **" + i['from'][-4:]
            elif "MasterCard" in i['from']:
                i['from'] = "MasterCard " + i['from'][11:15] + " **** **** " + i['from'][-4:]
    return new_list


def print_inference(new_list):
    """Подготавливает данные на печать и выводит их"""
    for i in new_list:
        print(i['date'], i['description'], "" if i.get('from') == None else i.get('from'), "->", i['to'],
          i['operationAmount']['amount'], i['operationAmount']['currency']['name'], end="\n\n")


all_operations = load_operations()
new_list = preparation_accounts(change_data(sorting_data(all_operations)))
print_inference(new_list)








