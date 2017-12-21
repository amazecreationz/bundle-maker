#!/usr/bin/env python
import json
from jsmin import jsmin

SETTINGS_FILE = "settings.json"
DATA = json.load(open(SETTINGS_FILE))
BUNDLE = DATA["bundle"]

OUTPUT = DATA["output"] + ".js"
OUTPUT_MIN = DATA["output"] + ".min.js"
OUTPUT_FILE = open(OUTPUT, "w+")
OUTPUT_MIN_FILE = open(OUTPUT_MIN, "w+")

for ITEM in BUNDLE:
	with open("js/" +ITEM) as INPUT_FILE:
		CONTENT = INPUT_FILE.read()
		OUTPUT_FILE.write(CONTENT + "\n\n")

OUTPUT_FILE.seek(0);
OUTPUT_MIN_FILE.write(jsmin(OUTPUT_FILE.read()))
OUTPUT_FILE.close();
OUTPUT_MIN_FILE.close()
print OUTPUT_MIN + " is ready."