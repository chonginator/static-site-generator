import os
import shutil
from copystatic import copydir

def main():
  src_path = "static"
  dst_path = "public"

  if os.path.exists(dst_path):
    shutil.rmtree(dst_path)

  copydir(src_path, dst_path)

main()