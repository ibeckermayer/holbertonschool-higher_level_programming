#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":

    req = requests.post("http://0.0.0.0:5000/search_user",
                        data={'q': "" if len(argv) < 2 else argv[1]})
    try:
        json_dict = req.json()
        if not json_dict:
            print("No result")
            exit()
        jsonid = json_dict.get("id")
        jsonname = json_dict.get("name")
        print("[{}] {}".format(jsonid, jsonname))
    except ValueError as e:
        print("Not a valid JSON")
