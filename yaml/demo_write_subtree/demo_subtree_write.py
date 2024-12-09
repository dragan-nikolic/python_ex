import yaml
import pprint

# read
print('--- read yaml ---')
fr = open("table.yml")
data = yaml.load(fr, Loader=yaml.Loader)
fr.close()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

# write subtree
print('--- write subtree ---')
fw = open("subtree_write.yml", "w")
yaml.dump(data['columns'], fw)
fw.close()
 
# read subtree
print('--- read subtree ---')
fs = open("subtree_write.yml")
data = yaml.load(fs, Loader=yaml.Loader)
fs.close()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
