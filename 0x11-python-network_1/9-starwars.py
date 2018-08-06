#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search=" + argv[1]
    req = requests.get(url)
    try:
        json_dict = req.json()
        results = json_dict.get("results")
        print("Number of results: {}".format(len(results)))
        for item in results:
            print(item.get("name"))
    except ValueError as e:
        print("Not a valid JSON")
