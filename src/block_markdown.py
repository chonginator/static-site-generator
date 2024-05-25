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
