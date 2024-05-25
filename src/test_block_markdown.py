import unittest
from block_markdown import (
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_quote,
  block_type_unordered_list,
  block_type_ordered_list,
  markdown_to_blocks,
  block_to_block_type,
)

class TestBlockMarkdown(unittest.TestCase):
  def test_markdown_to_blocks(self):
    markdown = '''
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
    '''

    self.assertListEqual(
      markdown_to_blocks(markdown),
      [
  "This is **bolded** paragraph",
  "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
  "* This is a list\n* with items"
      ]
    )

  def test_block_to_block_type_heading(self):
    block = "## This is a heading"
    self.assertEqual(block_to_block_type(block), block_type_heading)

  def test_block_to_block_type_code(self):
    block = "```\nThis is a code block\n```"
    self.assertEqual(block_to_block_type(block), block_type_code)

  def test_block_to_block_type_quote(self):
    block = "> This is a quote\n> This quote has two lines"
    self.assertEqual(block_to_block_type(block), block_type_quote)

  def test_block_to_block_type_unordered_list(self):
    block = "* This is an unordered list\n- This is a bullet point"
    self.assertEqual(block_to_block_type(block), block_type_unordered_list)

  def test_block_to_block_type_ordered_list(self):
    block = "1. This is an ordered list\n2. This is my second point"
    self.assertEqual(block_to_block_type(block), block_type_ordered_list)

  def test_block_to_block_type_paragraph(self):
    block = "This is a plain paragraph.\nThis is another line in the paragraph"
    self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
  unittest.main()