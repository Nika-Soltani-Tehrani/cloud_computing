from flask import Flask
from redis import Redis
import requests
import json
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

coin_name = os.getenv('coin_name')
api_key = os.getenv('api_key')
cache_timeout = os.getenv('cache_timeout')

@app.route("/")
def serving():
    headers = {
        'X-CoinAPI-Key': api_key,
    }
    print(headers)
    if (redis.exists(coin_name)) == False:
        response = requests.get('https://rest.coinapi.io/v1/assets/'+ coin_name , headers=headers)
        data_json = json.loads(response.text)
        redis.set(coin_name, json.dumps(data_json))
        redis.expire(coin_name, cache_timeout)
        print('does not exist')
    else:
        data_json = json.loads(redis.get(coin_name))
    
    return {
            'name': data_json[0]['name'],
            'price': data_json[0]['price_usd']
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('port'), debug=True)
