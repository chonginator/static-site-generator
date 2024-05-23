class HTMLNode:
  def __init__(
    self,
    tag: str | None=None,
    value: str | None=None,
    children: list["HTMLNode"] | None=None,
    props: dict[str, str] | None=None,
  ):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError("to_html method not implemented")

  def props_to_html(self):
    props_html = ""
    if self.props is None:
      return props_html

    for key, value in self.props.items():
      props_html += f" {key}=\"{value}\""
    
    return props_html

  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
  def __init__(
      self,
      tag: str | None=None,
      value: str | None=None,
      props: dict[str, str] | None=None
  ):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("Invalid HTML: no value")
    
    if self.tag is None:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
  def __init__(
      self,
      tag: str | None=None,
      children: dict[str, str] | None=None,
      props: dict[str, str] | None=None
  ):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("Invalid HTML: no tag")
    
    if self.children is None:
      raise ValueError("Invalid HTML: no children")

    children_html = "".join(map(lambda child: child.to_html(), self.children))
    return f"<{self.tag}>{children_html}</{self.tag}>"

  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}), {self.props}"
      