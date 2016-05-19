import yaml
import pprint

f = open("test.yml")
data = yaml.load(f)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)