import json

test_dict = {'string1': 123,
             'string2': 'value'
             }
json_text = json.dumps(test_dict)
print(json_text)
print(json.loads(json_text))
