import requests
import sys


try:
    response = requests.get("http://192.168.254.102/index.html?em")
    tags = response.text
    print(tags)
except Exception as e:
    print("[Error {0}]".format(e))