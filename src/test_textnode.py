import unittest

from textnode import (
  TextNode,
  TextType,
)

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.NORMAL)
    node2 = TextNode("This is a text node", TextType.NORMAL)

    self.assertEqual(node, node2)
  
  def test_not_eq(self):
    node = TextNode("This is a text node", TextType.NORMAL)
    node2 = TextNode("This is a text node", TextType.BOLD)

    self.assertNotEqual(node, node2)

  def test_not_eq2(self):
    node = TextNode("This is a text node", TextType.NORMAL)
    node2 = TextNode("This is also a text node", TextType.NORMAL)

    self.assertNotEqual(node, node2)

  def test_url_eq(self):
    node = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")
    node2 = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")

    self.assertEqual(node, node2)
  
  def test_url_none_eq(self):
    node = TextNode("This is a a text node", TextType.BOLD)
    node2 = TextNode("This is a a text node", TextType.BOLD, None)

    self.assertEqual(node, node2)

if __name__ == "__main__":
  unittest.main()