#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/users"
    req = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    json_dict = req.json()
    print(json_dict.get("id"))

    # try:
    #     json_dict = req.json()
    #     results = json_dict.get("results")
    #     print("Number of results: {}".format(len(results)))
    #     for item in results:
    #         print(item.get("name"))
    # except ValueError as e:
    #     print("Not a valid JSON")
