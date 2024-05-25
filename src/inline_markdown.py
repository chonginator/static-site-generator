import re

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_image,
  text_type_link,
)

def text_to_textnodes(text):
  nodes = [TextNode(text, text_type_text)]
  nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
  nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
  nodes = split_nodes_delimiter(nodes, "`", text_type_code)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)

  return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    
    split_text = old_node.text.split(delimiter)
    split_nodes = []

    if len(split_text) % 2 == 0:
      raise Exception("Invalid markdown, formatted section not closed")

    for i in range(len(split_text)):
      if split_text[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(split_text[i], text_type_text))
      else:
        split_nodes.append(TextNode(split_text[i], text_type))

    new_nodes.extend(split_nodes)

  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    
    images = extract_markdown_images(old_node.text)

    if len(images) == 0:
      new_nodes.append(old_node)
      continue
    
    current_section_text = old_node.text
    for image in images:
      sections = current_section_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)

      if sections[0] != "":
        new_nodes.append(TextNode(sections[0], text_type_text))
      
      new_nodes.append(TextNode(image[0], text_type_image, image[1]))

      current_section_text = sections[1]

    if current_section_text != "":
      new_nodes.append(TextNode(current_section_text, text_type_text))
  
  return new_nodes
    
def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    
    links = extract_markdown_links(old_node.text)

    if len(links) == 0:
      new_nodes.append(old_node)
      continue
    
    current_section_text = old_node.text
    for link in links:
      sections = current_section_text.split(f"[{link[0]}]({link[1]})", maxsplit=1)

      if sections[0] != "":
        new_nodes.append(TextNode(sections[0], text_type_text))
      
      new_nodes.append(TextNode(link[0], text_type_link, link[1]))

      current_section_text = sections[1]

    if current_section_text != "":
      new_nodes.append(TextNode(current_section_text, text_type_text))
  
  return new_nodes

def extract_markdown_images(text):
  matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return matches

def extract_markdown_links(text):
  matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
  return matches

