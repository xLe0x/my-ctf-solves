import requests
import base64
import json

session = requests.Session()

url = "https://7134d86238462086.247ctf.com/flag"

response = session.get(url)

session_cookie = response.cookies.get_dict()["session"]

# added by chatgpt to fix some padding issues
session_cookie += '=' * (-len(session_cookie) % 4)

decoded_session = base64.b64decode(session_cookie)
decoded_session = decoded_session.decode('utf-8', errors='ignore')

clean_json = decoded_session.split('}')[0] + '}}'

data = json.loads(clean_json)

flag_encoded = data["flag"][" b"]

flag = base64.b64decode(flag_encoded).decode()

print(flag)
