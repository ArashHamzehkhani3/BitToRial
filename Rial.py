import requests



def get_rial():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    ate = data['rates']['IRR']
    return ate


