"""
NOTE: IN PROGRESS

The utility for renaming all the files in a directory to the following name:
  <name_prefix>_<date_created>_<name_suffix>.ext
where 'ext' is file extension that does not change.
"""
import os
import sys
import re
import datetime

from PIL import Image
from PIL.ExifTags import TAGS

# --- Modify these variables to customize the renaming ---
NAME_PREFIX = 'new_'
NAME_SUFFIX = ''
# --------------------------------------------------------

try:
    dir_name = sys.argv[1]
except Exception:
    dir_name = "."

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

def get_file_date(path):
    # file modification
    timestamp = os.path.getmtime(path)
    
    # convert timestamp into DateTime object
    datestamp = datetime.datetime.fromtimestamp(timestamp)
    
    # file creation
    c_timestamp = os.path.getctime(path)
    
    # convert creation timestamp into DateTime object
    c_datestamp = datetime.datetime.fromtimestamp(c_timestamp)
    
    return datestamp, c_datestamp

def get_file_extension(path):
  return os.path.splitext(path)[1]

def is_image(path):
  ext = get_file_extension(path)
  print(ext)
  if ext in ('.jpeg', '.jpg'):
    return True

  return False

def get_image_metadata(path):
  if not is_image(path):
    print(path + " is not an image!")
    return {}

  image = Image.open(path)

  # extract other basic metadata
  info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
  }

  # extract EXIF data
  exifdata = image.getexif()

  # iterating over all EXIF data fields
  for tag_id in exifdata:
      # get the tag name, instead of human unreadable tag id
      tag = TAGS.get(tag_id, tag_id)
      data = exifdata.get(tag_id)
      # decode bytes 
      if isinstance(data, bytes):
          data = data.decode()

      info_dict[tag] = data

  return info_dict

def print_metadata(metadata):
  for label,value in metadata.items():
    print(f"{label:25}: {value}")


#------------- main ------------------------------------------------------------
for root, dirs, files in os.walk(dir_name):
    for filename in files:
        filepath = os.path.abspath(os.path.join(root, filename))
        print(filepath)
        print_metadata(get_image_metadata(filepath))
        print('---')
