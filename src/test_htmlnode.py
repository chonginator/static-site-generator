import unittest

from htmlnode import (
  HTMLNode,
  LeafNode,
  ParentNode,
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

class TestParentNode(BaseTestNode):
  def setUp(self):
    super().setUp()
    self.leaf_node_a = LeafNode("a", self.value, props=self.props)
    self.leaf_node_p = LeafNode("p", self.value)
    self.parent_node_p = ParentNode(
      "p",
      children=[self.leaf_node_a, self.leaf_node_p]
    )
  
  def test_to_html_no_tag(self):
    node = ParentNode(None, [self.leaf_node_a, self.leaf_node_p], None)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_no_children(self):
    node = ParentNode("p", None, None)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_with_only_leaf_nodes(self):
    self.assertEqual(
      self.parent_node_p.to_html(),
      (
        f"<p>"
          f"{self.leaf_node_a.to_html()}"
          f"{self.leaf_node_p.to_html()}"
        f"</p>"
      )
    )

  def test_to_html_leaf_nodes_with_raw_text(self):
    node = ParentNode(
      "p",
      [self.leaf_node_a, LeafNode(None, "hello, world"), self.leaf_node_p]
    )
    self.assertEqual(
      node.to_html(),
      (
        f"<p>"
          f"{self.leaf_node_a.to_html()}"
          f"{"hello, world"}"
          f"{self.leaf_node_p.to_html()}"
        f"</p>"
      )
    )

  def test_to_html_with_leaf_nodes_and_parent_nodes(self):
    node = ParentNode(
      "p",
      [self.leaf_node_a, self.leaf_node_p, self.parent_node_p]
    )
    self.assertEqual(
      node.to_html(),
      (
        f"<p>"
          f"{self.leaf_node_a.to_html()}"
          f"{self.leaf_node_p.to_html()}"
          f"<p>"
            f"{self.leaf_node_a.to_html()}"
            f"{self.leaf_node_p.to_html()}"
          f"</p>"
        f"</p>"
      )
    )

  def test_to_html_with_nested_parent_nodes(self):
    nested_p_node = ParentNode(
      "p",
      [self.parent_node_p]
    )
    node = ParentNode(
      "p",
      [self.leaf_node_a, self.leaf_node_p, nested_p_node]
    )
    self.assertEqual(
      node.to_html(),
      (
        f"<p>"
          f"{self.leaf_node_a.to_html()}"
          f"{self.leaf_node_p.to_html()}"
          f"<p>"
            f"<p>{self.leaf_node_a.to_html()}{self.leaf_node_p.to_html()}</p>"
          f"</p>"
        f"</p>"
      )
    )

if __name__ == "__main__":
  unittest.main()