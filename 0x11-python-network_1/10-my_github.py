#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/users"
    req = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    json_dict = req.json()
    print(json_dict.get("id"))
