import unittest
from htmlnode import HTMLNode
from block_markdown import (
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_quote,
  block_type_unordered_list,
  block_type_ordered_list,
  markdown_to_html_node,
  paragraph_to_html_node,
  heading_to_html_node,
  code_to_html_node,
  quote_to_html_node,
  unordered_list_to_html_node,
  ordered_list_to_html_node,
  markdown_to_blocks,
  block_to_block_type,
)

class TestBlockMarkdown(unittest.TestCase):
  def test_markdown_to_html_node(self):
    markdown = '''
# Front-End Development is the Worst

Look, front-end development is for **script kiddies and soydevs who can't handle the real programming**. I mean,
it's just a bunch of divs and spans, right? And css??? It's like, "Oh, I want this to be red, but not thaaaaat
red." What a joke.

Real programmers code, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not
Windows. They use Vim, not VS Code. They use C, not HTML. Come to the [backend](https://www.boot.dev), where the real programming
happens.

'''
    rootNode = markdown_to_html_node(markdown)
    expected_html = "<div><h1>Front-End Development is the Worst</h1><p>Look, front-end development is for <b>script kiddies and soydevs who can't handle the real programming</b>. I mean, it's just a bunch of divs and spans, right? And css??? It's like, \"Oh, I want this to be red, but not thaaaaat red.\" What a joke.</p><p>Real programmers code, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not Windows. They use Vim, not VS Code. They use C, not HTML. Come to the <a href=\"https://www.boot.dev\">backend</a>, where the real programming happens.</p></div>"

    self.assertEqual(rootNode.to_html(), expected_html)

  def test_markdown_paragraph_to_html_node(self):
    block = "This is a plain paragraph.\nThis is another line in the paragraph with a **bolded** word"
    node = paragraph_to_html_node(block)

    self.assertEqual(node.to_html(), "<p>This is a plain paragraph. This is another line in the paragraph with a <b>bolded</b> word</p>")

  def test_markdown_heading_to_html_node(self):
    block = "## This is a heading"
    node = heading_to_html_node(block)

    self.assertEqual(node.to_html(), "<h2>This is a heading</h2>")

  def test_markdown_code_to_html_node(self):
    block = "```\nThis is a code block\n```"
    node = code_to_html_node(block)

    self.assertEqual(node.to_html(), "<pre><code>This is a code block</code></pre>")

  def test_markdown_quote_to_html_node(self):
    block = '''> This is a\n> blockquote block'''
    node = quote_to_html_node(block)

    self.assertEqual(node.to_html(), "<blockquote>This is a blockquote block</blockquote>")

  def test_markdown_unordered_list_to_html_node(self):
    block = "* **This is** an unordered list\n- This is a bullet point"
    node = unordered_list_to_html_node(block)

    self.assertEqual(node.to_html(), "<ul><li><b>This is</b> an unordered list</li><li>This is a bullet point</li></ul>")

  def test_markdown_ordered_list_to_html_node(self):
    block = "1. This is an unordered list\n2. This is a bullet point"
    node = ordered_list_to_html_node(block)

    self.assertEqual(node.to_html(), "<ol><li>This is an unordered list</li><li>This is a bullet point</li></ol>")

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