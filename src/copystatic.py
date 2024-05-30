import os
import shutil

def copydir(src, dst):
  if not os.path.exists(src):
    raise ValueError("Source path does not exist")

  if not os.path.exists(dst):
    os.mkdir(dst)

  for entry in os.listdir(src):
    src_path = os.path.join(src, entry)
    dst_path = os.path.join(dst, entry)
    
    if os.path.isfile(src_path):
      shutil.copy(src_path, dst_path)
    else:
      copydir(src_path, dst_path)
