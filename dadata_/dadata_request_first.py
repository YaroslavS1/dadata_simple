import json
from typing import Dict

import requests
from config import API_KEY
from config import SECRET

BASE_URL = 'https://cleaner.dadata.ru/api/v1/clean/address'


def suggest(query: str) -> Dict[str, str]:
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {API_KEY}",
        "X-Secret": SECRET
    }

    res = requests.post(BASE_URL, data=json.dumps([query]), headers=headers)
    res_ = res.json()

    if len(res_) == 1 and isinstance(res_, list):
        return res_[0]
    elif isinstance(res_, dict):
        return res_
    else:
        raise AssertionError


def cli() -> None:
    while True:
        stuff_address = input()
        if len(stuff_address) == 0:
            break
        data = suggest(stuff_address)
        print(data['result'])


if __name__ == '__main__':
    cli()
