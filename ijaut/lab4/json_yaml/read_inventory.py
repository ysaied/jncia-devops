import yaml
import json

FILENAME = "inventory.yaml"

with open(FILENAME) as f:
    content = yaml.load(f)

print(json.dumps(content))
