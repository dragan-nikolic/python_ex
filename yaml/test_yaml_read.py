import yaml
import pprint

#f = open("test.yml")
f = open("table.yml")
data = yaml.load(f, Loader=yaml.Loader)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

print(data['column_distinct_values'][1])