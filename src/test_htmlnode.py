import unittest

from htmlnode import (
  HTMLNode,
  LeafNode
)

class BaseTestNode(unittest.TestCase):
  def setUp(self):
    self.href = "https://boot.dev"
    self.target = "_blank"
    self.props = {
      "href": self.href,
      "target": self.target
    }
    self.value = "Boot.dev"


class TestHTMLNode(BaseTestNode):
  def setUp(self):
    super().setUp()
    self.node_a = HTMLNode("a", self.value, props=self.props)
    self.node_p = HTMLNode("p", self.value)

  def test_props_to_html(self):
    self.assertEqual(self.node_a.props_to_html(), f" href=\"{self.href}\" target=\"{self.target}\"")

  def test_no_props_to_html(self):
    self.assertEqual(self.node_p.props_to_html(), "")

class TestLeafNode(BaseTestNode):
    def setUp(self):
      super().setUp()
      self.node_a = LeafNode("a", self.value, props=self.props)

    def test_to_html_no_children(self):
      self.assertEqual(
        self.node_a.to_html(),
        f"<a href=\"{self.href}\" target=\"{self.target}\">{self.value}</a>"
      )

    def test_to_html_no_value(self):
      node = LeafNode("a", None, props=self.props)
      with self.assertRaises(ValueError):
        node.to_html()

    def test_to_html_no_tag(self):
      node = LeafNode(None, self.value, self.props)
      self.assertEqual(node.to_html(), self.value)

if __name__ == "__main__":
  unittest.main()