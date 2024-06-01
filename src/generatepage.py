import os
import re
from pathlib import Path
from block_markdown import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  if not os.path.isdir(dir_path_content):
    raise ValueError(f"Content directory path is not a directory: {dir_path_content}")

  if os.path.isfile(dest_dir_path):
    raise ValueError(f"Invalid destination directory path: {dest_dir_path}")

  for entry in os.listdir(dir_path_content):
    entry_from_path = os.path.join(dir_path_content, entry)
    entry_dest_path = os.path.join(dest_dir_path, entry)

    if os.path.isfile(entry_from_path):
      if entry_from_path.endswith(".md"):
        entry_dest_path = Path(entry_dest_path).with_suffix(".html")
        generate_page(entry_from_path, template_path, entry_dest_path)
      else:
        continue
    else:
      generate_pages_recursive(entry_from_path, template_path, entry_dest_path)

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")

  markdown_file = open(from_path)
  markdown = markdown_file.read()
  markdown_file.close()

  template_file = open(template_path)
  template_html = template_file.read()
  template_file.close()

  html_node = markdown_to_html_node(markdown)
  html = html_node.to_html()

  title = extract_title(markdown)
  template = template_html.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", html)

  dest_dir_name = os.path.dirname(dest_path)
  is_dest_dir_root = dest_dir_name == ""

  if not is_dest_dir_root and not os.path.exists(dest_dir_name):
    os.makedirs(dest_dir_name)

  html_file = open(dest_path, "w")
  html_file.write(template)
  html_file.close()
  
def extract_title(markdown):
  titles = re.findall(r"^# (.*?)$", markdown, re.MULTILINE)

  if len(titles) == 0:
    raise Exception("Invalid markdown, no h1 present")
  
  return titles[0]
