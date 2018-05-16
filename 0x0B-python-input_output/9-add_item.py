#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    args = load_from_json_file(filename)
except:
    args = []

args += sys.argv[1:]
save_to_json_file(args, filename)
