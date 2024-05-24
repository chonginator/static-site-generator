from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code
)

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