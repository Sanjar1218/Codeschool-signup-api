import requests
import json

dct = {
            "t_first_name": "Sanjar",
            "t_username": "None",
            "data": {
                "first_name": "Sanjarbek",
                "last_name": "Saidov",
                "email": "asdf",
                "option": "Sun\u2019iy intillekt \"AI\" (Computer vision)."
            }
        }

r = requests.post('http://127.0.0.1:8000', json=dct)
print(r.json())