#!/usr/bin/python
import os
import re

import shutil

current_dir = os.getcwd()

for x in range(0, 4):
	for file in os.listdir(current_dir):
		if os.path.isfile(os.path.join(current_dir, file)) and not file.startswith("."):
			new_file = re.sub(r"^(.*?)\ ", "", file)
			shutil.move(os.path.join(current_dir,file), os.path.join(current_dir,new_file))
