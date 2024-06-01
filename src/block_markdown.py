import re

from textnode import text_node_to_html_node
from htmlnode import (
  LeafNode,
  ParentNode
)

from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  children = []
  for block in blocks:
    html_node = block_to_html_node(block)
    children.append(html_node)

  rootNode = ParentNode("div", children)
  return rootNode

def block_to_html_node(block):
  block_type = block_to_block_type(block)
  if block_type == block_type_paragraph:
    return paragraph_to_html_node(block)
  if block_type == block_type_heading:
    return heading_to_html_node(block)
  if block_type == block_type_quote:
    return quote_to_html_node(block)
  if block_type == block_type_code:
    return code_to_html_node(block)
  if block_type == block_type_unordered_list:
    return unordered_list_to_html_node(block)
  if block_type == block_type_ordered_list:
    return ordered_list_to_html_node(block)
  raise ValueError("Invalid block type")

def paragraph_to_html_node(paragraph):
  lines = paragraph.split("\n")
  paragraph = " ".join(lines)
  children = text_to_children(paragraph)

  return ParentNode("p", children, None)

def heading_to_html_node(heading):
  heading_level = heading.count("#")
  if heading_level > 6:
    raise ValueError(f"Invalid heading level: {heading_level}")

  heading_text = heading.lstrip("# ")
  children = text_to_children(heading_text)

  return ParentNode(f"h{heading_level}", children, None)

def code_to_html_node(code):
  if not code.startswith("```") or not code.endswith("```"):
    raise ValueError("Invalid code block")

  cleaned_code = text_to_children(code.strip("`\n"))
  chidlren = ParentNode("code", cleaned_code)
  return ParentNode("pre", [chidlren], None)

def quote_to_html_node(quote):
  lines = quote.split("\n")
  if all(not line.startswith(">") for line in lines):
    raise ValueError("Invalid quote block")

  cleaned_quote = " ".join(line.strip("> ") for line in lines)
  children = text_to_children(cleaned_quote)
  return ParentNode("blockquote", children, None)

def unordered_list_to_html_node(unordered_list):
  lines = [re.sub(r"^[*|-] ", "", line) for line in unordered_list.split("\n")]
  list_items = [ParentNode("li", text_to_children(line), None) for line in lines]

  return ParentNode("ul", list_items, None)

def ordered_list_to_html_node(ordered_list):
  cleaned_string = re.sub(r"\d+\. ", "", ordered_list, flags=re.MULTILINE)
  lines = cleaned_string.split("\n")
  list_items = [ParentNode("li", text_to_children(line), None) for line in lines]

  return ParentNode("ol", list_items, None)

def text_to_children(text):
  return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def markdown_to_blocks(markdown):
  blocks = markdown.strip().split("\n\n")
  non_empty_blocks = list(filter(lambda block: block != "", blocks))

  stripped_non_empty_blocks = [block.strip() for block in non_empty_blocks]
  
  return stripped_non_empty_blocks

def block_to_block_type(block):
  if is_heading(block):
    return block_type_heading
  elif is_code_block(block):
    return block_type_code
  elif is_quote(block):
    return block_type_quote
  elif is_unordered_list(block):
    return block_type_unordered_list
  elif is_ordered_list(block):
    return block_type_ordered_list
  else:
    return block_type_paragraph

def is_heading(block):
  return re.match(r"^#{1,6} .+?$", block)

def is_code_block(block):
  lines = block.split("\n")
  return (
    len(lines) > 1
    and lines[0].startswith("```")
    and lines[-1].startswith("```")
  )

def is_quote(block):
  lines = block.split("\n")
  return all(re.match(r"^>.*?$", line) for line in lines)

def is_unordered_list(block):
  lines = block.split("\n")
  return all(re.match(r"^[*-] .*?$", line) for line in lines)

def is_ordered_list(block):
  lines = block.split("\n")
  return all(re.match(rf"^{i+1}. .*?$", line) for i, line in enumerate(lines))
  

