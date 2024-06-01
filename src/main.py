import os
import shutil
from copystatic import copydir
from generatepage import (extract_title, md, generate_page)

def main():
  src_path = "static"
  dst_path = "public"

  if os.path.exists(dst_path):
    shutil.rmtree(dst_path)

  copydir(src_path, dst_path)

  generate_page("content/index.md", "template.html", "public/index.html")
  

main()