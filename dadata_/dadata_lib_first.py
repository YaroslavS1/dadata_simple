from dadata import Dadata

API_KEY = '7d3e6e03fab9cfa6f1079bbde3ff52a54801d772'
BASE_URL = 'https://cleaner.dadata.ru/api/v1/clean/address'
SECRET = "520c4dcfcab05aee14e1e0dca8e504738518b12d"

dadata = Dadata(API_KEY, SECRET)
result = dadata.clean("address", "мск сухонска 11/-89")
print(result['result'])



