import json
from pprint import pprint
json_example = open("JSON_Example.json",'r').read()
pprint(json_example)
json_python = json.loads(json_example)
pprint(json_python)
int_name=json_python["ietf-interfaces"]["ietf-ip:ipv4"]["address"][1]["mask"]
pprint(int_name)
json_json=json.dumps(json_python)
pprint(json_json)
