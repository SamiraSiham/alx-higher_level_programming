#!/usr/bin/python3
'''add_item module'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    old_stuff = load_from_json_file('add_item.json')
except Exception:
    old_stuff = []

old_stuff.extend(arglist)
save_to_json_file(old_stuff, 'add_item.json')
