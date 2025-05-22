import requests

url = "http://127.0.0.1:8000/api/v1/split"
success_data = {
    "count"    : 3,
    "amount"   : 1000,
    "delimiter": ","
}

error_data = {
    "count"    : 0,
    "amount"   : 100,
    "delimiter": ","
}

success_response = requests.post(url, json=success_data)
print(success_response.json())

error_response = requests.post(url, json=error_data)
print(error_response.json())