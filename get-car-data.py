import requests
import json
import time

def fetch(count):
    response = requests.get(f"https://api-sell24.cars24.team/buy-used-car?sort=P&serveWarrantyCount=true&gaId=378858094.1642614426&page={count}&storeCityId=5732")
    if response.status_code == 200:
        data = response.json()
        with open('data-py.json', 'a', encoding='utf-8') as file:
            json.dump(data['data']['content'], file)
            file.write(',')
        print('Saved!')
        count += 1
        if count < 5:
            fetch(count)
    else:
        print(f"Failed to fetch data for page {count}")
        time.sleep(5)
        fetch(count)

fetch(1)
