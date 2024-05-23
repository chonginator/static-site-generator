from enum import Enum

text_type_normal = "normal"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
  def __init__(self, text: str, text_type: str, url: str | None=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other: "TextNode"):
    return (
      self.text == other.text
      and self.text_type == other.text_type
      and self.url == other.url
    )

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"