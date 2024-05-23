import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def setUp(self):
    self.href = "https://boot.dev"
    self.target = "_blank"
    self.props = {
      "href": self.href,
      "target": self.target
    }
    self.value = "Boot.dev"
    self.node_a = HTMLNode("a", self.value, props=self.props)
    self.node_p = HTMLNode("p", self.value)

  def test_props_to_html_eq(self):
    self.assertEqual(self.node_a.props_to_html(), f" href=\"{self.href}\" target=\"{self.target}\"")

  def test_no_props_to_html_eq(self):
    self.assertEqual(self.node_p.props_to_html(), "")

if __name__ == "__main__":
  unittest.main()