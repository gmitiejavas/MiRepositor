import yaml
from pprint import pprint
yaml_example = open("YAML-Example.yaml",'r').read()
pprint(yaml_example)
yaml_python = yaml.load(yaml_example)
pprint(yaml_python)
int_name=yaml_python["ietf-interface:interface"]["ietf-ip:ipv4"]["address"][1]["netmask"]
pprint(int_name)
yaml_yaml=yaml.dump(yaml_python)
pprint(yaml_yaml)
