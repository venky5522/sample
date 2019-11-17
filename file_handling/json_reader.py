import json
with open(r"C:\Users\pravallika p\Desktop\data.json","r") as json_file:
    data = json.load(json_file)
    for p in data["people"]:
        print('Name: '+p['name'])
        print('Website: '+p['website'])
        print('From: '+p['from'])





