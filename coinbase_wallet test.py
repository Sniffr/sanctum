# import requests
#
#
# def getbuyexchange():
#     url = "https://openexchangerates.org/api/latest.json?app_id=22246865dbbb47ac9f99b967d7a42ef7&symbols=KES"
#     # pass authorization token obtained during authentication in headers
#     headers = {
#         'Content-Type': "application/json",
#     }
#     response = requests.request("GET", url, headers=headers)
#     # Print response data
#     data = response.json()
#     print(data)
#     return data['rates']['KES']
#
# def getbuyexchange():
#     url = "https://free.currconv.com/api/v7/convert?q=USD_KES&apiKey=759ee01132696f2ea5f6"
#     # pass authorization token obtained during authentication in headers
#     headers = {
#         'Content-Type': "application/json",
#     }
#     response = requests.request("GET", url, headers=headers)
#     # Print response data
#     data = response.json()
#     return data['results']['USD_KES']['val']
import hashlib
import uuid

import requests


def test_auth():
    url = "https://api-test.spektra.co/oauth/token?grant_type=client_credentials"
    # pass authorization token obtained during authentication in headers
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic ZWExOGY5ODI2ZjAxNDZlYWIzZGRlZjYwNGY0NzEzODM6OGEwMWM0MDhlMjI2NDBhYmFkNWE2OGYzYTVjYzYwMjEzNGUzOTRmNTZkOGU0NDQ2YTQ5OTZhOWMzYWJiOTcyZg=="
    }
    response = requests.request("POST", url, headers=headers)
    # Print response data
    data = response.json()

    return data["access_token"]

def gen_checkout_id(order_id):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + order_id.encode()).hexdigest() + '=' + salt


def check_id(hashed_password, order_id):
    password, salt = hashed_password.split('=')
    return password == hashlib.sha256(salt.encode() + order_id.encode()).hexdigest()


print(gen_checkout_id("42e8a3f6-3760-4040-a920-e042375694c5"))
