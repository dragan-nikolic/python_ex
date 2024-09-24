import yaml
import pprint

# read
print('--- read yaml ---')
fr = open("demo_anchors.yml")
data = yaml.load(fr, Loader=yaml.Loader)
fr.close()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

# write new yml
print('--- write to new yml ---')
fw = open("demo_anchors_write.yml", "w")
yaml.dump(data, fw)
fw.close()
