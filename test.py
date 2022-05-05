import requests
import json


def main():
    url = "http://127.0.0.1:8000/items/"
    body = {
        "name": "soccer_ball",
        "description": "this is goot soccer ball",
        "price": 10000,
        "tax": 1.1,
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()
