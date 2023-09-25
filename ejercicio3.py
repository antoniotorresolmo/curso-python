import requests
import json

URL = "https://faas-fra1-afec6ce7.doserverless.co/api/v1/web/fn-1f1056ff-de8e-4509-9811-27a68419f504/default/add"

def test(a, b):
    params = {'a':a, 'b':b}
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(URL, headers=headers, json=params)

    if 'result' not in response.text:
        raise Exception("No hay resultado")

    return int(json.loads(response.text)["result"])

print(test(1,1))

assert test(1,1) == 2
assert test(0,1) == 1