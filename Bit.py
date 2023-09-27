import requests

def get_bit():
    
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data=response.json()

    if "bitcoin" in data :
        bit_price=data['bitcoin']['usd']
        return bit_price
    

