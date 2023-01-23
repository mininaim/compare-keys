# Compare keys (and nested keys) in two JSON files, and print out any keys that are missing from either file.

import json

def compare_keys(obj1, obj2):
  for key in obj1:
    if isinstance(obj1[key], dict):
      compare_keys(obj1[key], obj2[key])
    elif key not in obj2:
      print('"%s" is missing from second object' % key)
  for key in obj2:
    if isinstance(obj2[key], dict):
      compare_keys(obj1[key], obj2[key])
    elif key not in obj1:
      print('"%s" is missing from first object' % key)


with open('ar.json') as f1:
  data1 = json.load(f1)

with open('en.json') as f2:
  data2 = json.load(f2)

compare_keys(data1, data2)