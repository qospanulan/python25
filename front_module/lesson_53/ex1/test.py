import requests

data = requests.get(
    url="https://reqres.in/api/users",
    headers={
        "x-api-key": "reqres-free-v1"
    }
)

print(data.json())

