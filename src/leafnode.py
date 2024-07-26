from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        if value == None:
            raise ValueError("A value must be passed!")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("A value must be passed boi!")

        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"