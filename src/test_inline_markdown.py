import unittest

from inline_markdown import (
  text_to_textnodes,
  split_nodes_delimiter,
  split_nodes_image,
  split_nodes_link,
  extract_markdown_images,
  extract_markdown_links,
)

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_image,
  text_type_link,
)


class TestInlineMarkdown(unittest.TestCase):
  def test_text_to_textnodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)

    self.assertListEqual(
      nodes,
      [
        TextNode("This is ", text_type_text),
        TextNode("text", text_type_bold),
        TextNode(" with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word and a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" and an ", text_type_text),
        TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and a ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev"),
      ]
    )

  def test_no_closing_delim(self):
    node = TextNode("This is text with a **bolded word missing a delimeter", text_type_text)

    with self.assertRaises(Exception):
      split_nodes_delimiter([node], "**", text_type_bold)

  def test_delim_bold(self):
    node = TextNode("This is text with a **bolded** word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

    self.assertListEqual(
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word", text_type_text),
        ],
        new_nodes,
    )

  def test_delim_bold_double(self):
    node = TextNode(
        "This is text with a **bolded** word and **another**", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word and ", text_type_text),
            TextNode("another", text_type_bold),
        ],
        new_nodes,
    )

  def test_delim_bold_multiword(self):
    node = TextNode(
        "This is text with a **bolded word** and **another**", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded word", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_bold),
        ],
        new_nodes,
    )

  def test_delim_italic(self):
    node = TextNode("This is text with an *italic* word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
    self.assertListEqual(
        [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ],
        new_nodes,
    )

  def test_delim_code(self):
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    self.assertListEqual(
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ],
        new_nodes,
    )

  def test_split_nodes_image_single(self):
    node = TextNode(
      "This is text with only one ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
      text_type_text,
    )

    new_nodes = split_nodes_image([node])

    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with only one ", text_type_text),
        TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
      ]
    )

  def test_split_nodes_image(self):
    node = TextNode(
      "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
      text_type_text,
    )

    new_nodes = split_nodes_image([node])

    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with an ", text_type_text),
        TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and another ", text_type_text),
        TextNode(
          "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
        ),
      ]
    )

  def test_split_nodes_link(self):
    node = TextNode(
      "This is text with a [link](https://www.example.com) and another [link](https://www.example.com/another)",
      text_type_text,
    )

    new_nodes = split_nodes_link([node])

    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("link", text_type_link, "https://www.example.com"),
        TextNode(" and another ", text_type_text),
        TextNode(
          "link", text_type_link, "https://www.example.com/another"
        ),
      ]
    )

  def test_extract_markdown_images(self):
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    images = extract_markdown_images(text)

    self.assertListEqual(images, [
      ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
    ])

  def test_extract_markdown_links(self):
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    links = extract_markdown_links(text)

    self.assertListEqual(links, [
      ("link", "https://www.example.com"),
      ("another", "https://www.example.com/another")
    ])

if __name__ == "__main__":
  unittest.main()