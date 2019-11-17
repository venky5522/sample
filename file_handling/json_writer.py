#java script object notation.
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

Get_path = r"C:\Users\pravallika p\Desktop\data.json"
with open(r"C:\Users\pravallika p\Desktop\data.json","w") as json_file:
    json.dump(data,json_file)
print(data)
