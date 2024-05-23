# pip install pyyaml

import yaml

filename = "data.yaml"

with open(filename) as fh:
    data = yaml.load(fh, Loader=yaml.Loader)

#print(data)
#print(data["Modules"])

for module in data["Modules"]:
    print(module)
