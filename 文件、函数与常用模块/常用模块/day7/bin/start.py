import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('luffy.json')))

f = open('%s/account/luffy.json'%(BASE_DIR))
date = json.load(f)
print(date)