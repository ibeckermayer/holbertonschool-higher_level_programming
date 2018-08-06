#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/users"
    data = {"username": argv[0], "password": argv[1]}
    req = requests.get(url, data=data)
    json_dict = req.json()[0]
    print(json_dict.get("id"))

    # try:
    #     json_dict = req.json()
    #     results = json_dict.get("results")
    #     print("Number of results: {}".format(len(results)))
    #     for item in results:
    #         print(item.get("name"))
    # except ValueError as e:
    #     print("Not a valid JSON")
