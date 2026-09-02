import json


string_json_data='{"name":"tete" , "iscat" : true , "micecaught" : 0 , "felineIQ": null  }'



json_data_as_python_value=json.loads(string_json_data)

print(type(json_data_as_python_value))


python_dict={'name': 'tete', 'iscat': True, 'micecaught': 0, 'felineIQ': None}

string=json.dumps(python_dict)

print(string)