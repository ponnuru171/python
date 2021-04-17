import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
print(len(r.json()['data']))

rdata = r.json()["data"].split(",")
count = 0
for data in rdata:
    split_data = data.split("=")
    if split_data[0].strip() == 'age' and int(split_data[1]) >= 50:
        count = count + 1
print(count)