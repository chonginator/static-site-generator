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
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
