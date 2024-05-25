import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
  blocks = markdown.strip().split("\n\n")
  non_empty_blocks = list(filter(lambda block: block != "", blocks))

  stripped_non_empty_blocks = list(
    map(
      lambda block: block.strip(),
      non_empty_blocks
    )
  )

  return stripped_non_empty_blocks

def block_to_block_type(markdown_block):
  if is_heading(markdown_block):
    return block_type_heading
  elif is_code_block(markdown_block):
    return block_type_code
  elif is_quote(markdown_block):
    return block_type_quote
  elif is_unordered_list(markdown_block):
    return block_type_unordered_list
  elif is_ordered_list(markdown_block):
    return block_type_ordered_list
  else:
    print(f"block: {markdown_block}")
    return block_type_paragraph

def is_heading(markdown_block):
  return re.match(r"^#{1,6} .+?$", markdown_block)

def is_code_block(markdown_block):
  lines = markdown_block.split("\n")
  return (
    len(lines) > 1
    and lines[0].startswith("```")
    and lines[-1].startswith("```")
  )

def is_quote(markdown_block):
  lines = markdown_block.split("\n")
  return all(re.match(r"^>.*?$", line) for line in lines)

def is_unordered_list(markdown_block):
  lines = markdown_block.split("\n")
  return all(re.match(r"^[*-] .*?$", line) for line in lines)

def is_ordered_list(markdown_block: str):
  lines = markdown_block.split("\n")
  return all(re.match(rf"^{i+1}. .*?$", line) for i, line in enumerate(lines))
  

