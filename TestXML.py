import yaml
import xmltodict
from pprint import pprint
xml=open("XML-Example.xml").read()
print(type(xml))
print(xml)
xml_dict=xmltodict.parse(xml)
pprint(xml_dict)
print(type(xml_dict))
print(xml_dict["interface"]["ipv4"]["address"][1]["ip"])
