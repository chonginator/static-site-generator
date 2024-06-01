import os
import shutil
from copystatic import copydir
from generatepage import (generate_page, generate_pages_recursive)

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
  print("Deleting public directory...")
  if os.path.exists(dir_path_public):
    shutil.rmtree(dir_path_public)

  print(f"Copying static files to public directory...")
  copydir(dir_path_static, dir_path_public)

  print("Generating pages...")
  generate_pages_recursive(dir_path_content, template_path, dir_path_public)
  
main()