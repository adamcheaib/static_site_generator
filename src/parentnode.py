from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode
import unittest
import re


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Cannot have an empty tag for parent")
        if self.children == None:
            raise ValueError("Must contain children!")

        children = ""
        for child in self.children:
            children += child.to_html()

        return f"<{self.tag}>{children}</{self.tag}>"

    def __eq__(self, other):
        return self.tag == other.tag and self.tag == other.tag and self.children == other.children and self.props == other.props


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def text_node_to_html_node(text_node):
    tag = None
    if text_node.text_type == text_type_bold:
        tag = "b"
    elif text_node.text_type == text_type_italic:
        tag = "i"
    elif text_node.text_type == text_type_code:
        tag = "code"
    elif text_node.text_type == text_type_link:
        tag = "a"
    elif text_node.text_type == text_type_image:
        tag = "img"

    print(tag)
    return LeafNode(tag, text_node.links_text, None)

