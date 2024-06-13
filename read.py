import json
with open ("Subdomain.json") as f:
    data = json.load(f)
    print(type(data['Content'][1]))
    print(data['Content'][1])
    my_dict = json.loads(data['Content'][1])
    print(type(my_dict))
    print(my_dict['data'])
