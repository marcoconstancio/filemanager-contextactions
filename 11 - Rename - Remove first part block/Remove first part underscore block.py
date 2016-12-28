#!/usr/bin/python
import os
import re

import shutil

current_dir = os.getcwd()

for file in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, file)) and not file.startswith("."):

        new_file = re.sub(r"^(.*?)\_", "", file)

        #print(os.path.join(current_dir,file) + " -> "+ os.path.join(current_dir,new_file) )

        shutil.move(os.path.join(current_dir,file), os.path.join(current_dir,new_file))
