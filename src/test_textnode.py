import unittest

from textnode import (
  TextNode,
  text_type_normal,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_image,
  text_type_link,
)

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", text_type_normal)
    node2 = TextNode("This is a text node", text_type_normal)

    self.assertEqual(node, node2)
  
  def test_not_eq(self):
    node = TextNode("This is a text node", text_type_normal)
    node2 = TextNode("This is a text node", text_type_bold)

    self.assertNotEqual(node, node2)

  def test_not_eq2(self):
    node = TextNode("This is a text node", text_type_normal)
    node2 = TextNode("This is also a text node", text_type_normal)

    self.assertNotEqual(node, node2)

  def test_url_eq(self):
    node = TextNode("This is a text node", text_type_italic, "https://boot.dev")
    node2 = TextNode("This is a text node", text_type_italic, "https://boot.dev")

    self.assertEqual(node, node2)
  
  def test_url_none_eq(self):
    node = TextNode("This is a a text node", text_type_bold)
    node2 = TextNode("This is a a text node", text_type_bold, None)

    self.assertEqual(node, node2)

if __name__ == "__main__":
  unittest.main()