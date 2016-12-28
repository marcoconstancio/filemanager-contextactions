#!/usr/bin/python
import os
import re

import os, sys, getopt
from PIL import Image, ImageOps
current_dir = os.getcwd()



def main(argv):
    CURRENT_DIR = current_dir

    IMAGE_FORMATS = ('.jpg', '.jpeg', '.bmp', '.gif', '.png')
    SUB_DIRECTORY = "thumbs"
    HEIGHT = 200
    WIDTH = 200
    JPEG_QUALITY = 85

    FIT = "top_center" # no option selected, uses thumbnail instead of fit (cropping) function

    IGNORE_LIST = ('thumbs')
    OVERWRITE = 1

    CONTINUE = 1

    try:
        opts, args = getopt.getopt(argv,"vd:h:w:i:c:o:s:q",["dir=","height=","width=","ignore=","centering=","overwrite","subfolder=","jpgquality="])
    except getopt.GetoptError:
        print (getopt.GetoptError.message)
        print ('generate_thumb.py -d <dir_to_scan>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-v':
            print ('test.py -d <dir_to_scan>')
            sys.exit()
        elif opt in ("-d", "--dir"):
            CURRENT_DIR = arg
        elif opt in ("-h", "--height"):
            HEIGHT = int(arg)
        elif opt in ("-w", "--width"):
            WIDTH = int(arg)
        elif opt in ("-i", "--ignore"):
            IGNORE_LIST = arg.split(",")
        elif opt in ("-c", "--centering"):
            FIT = arg
        elif opt in ("-o", "--overwrite"):
            OVERWRITE = 1
        elif opt in ("-q", "--jpgquality"):
            JPEG_QUALITY = arg
        elif opt in ("-s", "--subfolder"):
            SUB_DIRECTORY = arg

    THUMB_SIZE = HEIGHT, WIDTH

    if FIT == 'top_left':
        FIT = (0.0,0.0)
    elif FIT == 'top_center':
        FIT = (0.5,0.0)
    elif FIT == 'top_right':
        FIT = (1.0,0.0)
    elif FIT == 'middle_left':
        FIT = (0.0,0.5)
    elif FIT == 'middle_center':
        FIT = (0.5,0.5)
    elif FIT == 'middle_right':
        FIT = (1.0,0.5)
    elif FIT == 'bottom_left':
        FIT = (0.0,1.0)
    elif FIT == 'bottom_center':
        FIT = (0.5,1.0)
    elif FIT == 'bottom_right':
        FIT = (1.0,1.0)

    for root, subdirs, files in os.walk(CURRENT_DIR):
        for file in files:
            if os.path.splitext(file)[1].lower() in IMAGE_FORMATS:
                for ignore in IGNORE_LIST:
                    if(ignore in subdirs):
                        subdirs.remove(ignore)

                if not os.path.exists(os.path.join(root, "thumbs")):
                    os.mkdir(os.path.join(root, "thumbs"))
                    print ("Creating thumbs dir.")

                filename = os.path.join(root, file)
                thumb_filename = os.path.join(root, SUB_DIRECTORY ,file)

                if not OVERWRITE and os.path.exists(thumb_filename):
                        CONTINUE = 0

                if CONTINUE:
                    try:
                        im = Image.open(filename)
                        #im.thumbnail((400,400))
                        #im.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
                        #im.fit(THUMB_SIZE, Image.ANTIALIAS)
                        if FIT:
                            im = ImageOps.fit(im, THUMB_SIZE, method = Image.ANTIALIAS, centering = FIT)
                        else:
                            #im.thumbnail((400,400))
                            im.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

                        #print(os.path.join(root, "thumbs", file))
                        if os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.jpeg':
                            #im.save(os.path.join(root, "thumbs" ,file), 'JPEG', quality=JPEG_QUALITY)
                            im.save(thumb_filename, 'JPEG', quality=JPEG_QUALITY)

                            print ("Saved " + thumb_filename)
                        else:
                            #im.save(os.path.join(root, "thumbs" ,file))
                            pass

                    except Exception as e:
                        print (e)
                        print ("Error converting: " + filename)

if __name__ == "__main__":
   main(sys.argv[1:])
