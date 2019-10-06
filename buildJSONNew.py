import csv
import json
from collections import defaultdict

csv_file = "filteredForJSON2.csv"
json_file = "dataJSON2.json"

import pkgutil
import encodings
import os

fields = []
rows = []
value = 1

json_data = {
    "name": "Criminal Offense",
    "children": list()
}

def doSomething(curr_dict, keys, key_index, data):
    # print()

    found = False
    for child in curr_dict: #list of children
        #print(curr_dict)
        if child["name"] == keys[key_index]:
            found = True

            if key_index < len(keys)-1:
                doSomething(child["children"], keys, key_index + 1, data)
            elif key_index == len(keys)-1:
                #print(value)
                if (int(value) > 2):
                    child["children"].append({
                        "name": data[0],
                        "value": value
                    })

    if not found and key_index < len(keys)-1:
        if (int(value) > 2):
            curr_dict.append({
                "name": keys[key_index],
                "children": list()
            })
    elif not found and key_index == len(keys)-1:
        if (int(value) > 2):
            curr_dict.append({
                "name": keys[key_index],
                "children": [{
                    "name": data[0],
                    "value": value
                }]
            })



with open(csv_file, "r", encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)

        
    for i,row in enumerate(reader):
        year = row['Year']
        street = row['Street']
        crime = row['Crime']
        
        value = row['Quantity']

        keys = [year, street]
        data = [crime]

        #print(keys)
        #print(data)

        doSomething(json_data["children"], keys, 0, data)

    with open(json_file, 'w') as fp:
        json.dump(json_data, fp)



