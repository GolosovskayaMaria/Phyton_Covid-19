print("\n")

import requests
import json
import pandas as pd
import numpy as np

country = 'russia'

api_url = 'https://api.api-ninjas.com/v1/covid19?country={}'.format(country)
api_key = {'X-Api-Key': 'OGP92iB7/coaWwFrV2BjQQ==znplhtLWD656A2hZ'}
response = requests.get(api_url, api_key)
response_json = response.json()

country = response_json[0]
cases = country['cases']
print(country['country'], "cases: ", cases, "\n")

n = 50
#1 x = 0
for case_num in range(46, min(n, len(cases))):
#1    x = x + 1
    case_key = list(cases)[case_num]
    case_val = list(cases.values())[case_num]
    case_key_prev = list(cases)[case_num-1]
    case_val_prev = list(cases.values())[case_num-1]
    death_val = case_val['total'] - case_val_prev['total']
    sick_val = case_val['total'] - case_val['new']
    if 'total' and 'new' in case_val:
        string = case_key, sick_val, case_val['new'], case_val['total'], death_val
        print(pd.DataFrame(string, index=['Дата:', 'Болеют:', 'Новые:', 'Всего:', 'Смертей за 2 дня:'],
                           columns=['Случаи заражения:']), "\n")
