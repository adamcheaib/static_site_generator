import unittest
from parentnode import ParentNode
from htmlnode import HTMLNode

markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""


def markdown_to_blocks(markdown):
    filtered_blocks = []
    stripped = markdown.split("\n\n")
    for item in stripped:
        if item == "":
            continue
        filtered_blocks.append(item.strip())
    return filtered_blocks


formatted_markdown = markdown_to_blocks(markdown)


def identify_block_type(block_line):
    characters = [
        "# ",
        "## ",
        "### ",
        "#### ",
        "##### ",
        "###### ",
        "```",
        "> ",
        "* ",
        "- ",
        "1. "
    ]

    type = "paragraph"
    for i in range(0, len(characters)):
        character = characters[i]
        if block_line.startswith(character):
            if (character == "# "
                    or character == "## "
                    or character == "### "
                    or character == "#### "
                    or character == "##### "
                    or character == "###### "):
                type = f"heading {i + 1}"

            if character == "```":
                type = "code"

            if character == "> ":
                type = "quote"

            if character == "* " or character == "- ":
                type = "unordered_list"

            if character == "1. ":
                type = "ordered_list"

    return type

def block_type_to_tag(block_type):
    if "heading" in block_type:
        heading_number = block_type.split(" ")[1]
        return f"h{heading_number}"

    if block_type == "code":
        return "code"

    if block_type == "quote":
        return "blockquote"

    if block_type == "unordered_list":
        return "ul"

    if block_type == "ordered_list":
        return "ol"

def markdown_to_html_node(markdown):
    cleansed_markdown = markdown_to_blocks(markdown)
    parent_element = ParentNode("div", [], None)
    for block in cleansed_markdown:
        block_type = identify_block_type(block)
        block_tag = block_type_to_tag(block_type)
        parent_element.children.append(HTMLNode(block_tag, block))

    return parent_element

markdown_to_html_node(markdown)
