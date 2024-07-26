from textnode import TextNode
from parentnode import text_type_text, text_type_italic, text_type_image, text_type_bold, text_type_code, text_type_link
import re
import unittest


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        separated_text = node.text.split(delimiter)
        if len(separated_text) % 2 == 0:
            raise ValueError("Missing closing for formatting!")

        for i in range(len(separated_text)):
            if i % 2 == 0:
                new_node_list.append(TextNode(separated_text[i], node.text_type, None))
            else:
                new_node_list.append(TextNode(separated_text[i], text_type, None))
    return new_node_list


test_case = [
    TextNode("The world will **shatter**!", "text", None),
    TextNode("The world will shatter!", "text", None),
    TextNode("You will **succumb** to me!", "text", None),
]

split_nodes_delimiter(test_case, "**", "bold")


def extract_markdown_images(text):
    return re.findall("\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall("\[(.*?)\]\((.*?)\)", text)


links_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
images_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

test_links_markdown = extract_markdown_links(links_text)

test_images_markdown = extract_markdown_images(images_text)

images_test_node = TextNode(images_text, text_type_text, None)
links_test_node = TextNode(links_text, text_type_text, None)


def split_nodes_image(old_nodes):
    new_nodes_list = []

    for old_node in old_nodes:
        original_text = old_node.text
        if original_text == "":
            continue
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_nodes_list.append(old_node)
            continue

        for image in images:
            if len(image) == 0:
                new_nodes_list.append(old_node)
                continue

            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

            if len(sections) != 2:
                raise ValueError("Image tag not closed or opened properly!")

            if sections[0] != "":
                new_nodes_list.append(TextNode(sections[0], text_type_text))

            new_nodes_list.append(TextNode(image[0], text_type_image, image[1]))

            if sections[1] != "":
                original_text = sections[1]
                new_nodes_list.append(TextNode(original_text, text_type_text))

    return new_nodes_list


def split_nodes_link(old_nodes):

    new_nodes_list = []

    for old_node in old_nodes:
        original_text = old_node.text
        if original_text == "":
            continue
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes_list.append(old_node)
            continue

        for link in links:
            if len(link) == 0:
                new_nodes_list.append(old_node)
                continue

            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(sections) != 2:
                raise ValueError("Link tag not closed or opened properly!")

            if sections[0] != "":
                new_nodes_list.append(TextNode(sections[0], text_type_text))

            new_nodes_list.append(TextNode(link[0], text_type_link, link[1]))

            if sections[1] != "":
                original_text = sections[1]
                new_nodes_list.append(TextNode(original_text, text_type_text))


    return new_nodes_list


test_str = "This is **bold text** with an *italic text* word and a `code block example` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
final_result = TextNode(test_str, text_type_text)

def text_to_textnodes(text_nodes):
    replace_bold = split_nodes_delimiter(text_nodes, "**", "bold")

    replace_italic = split_nodes_delimiter(replace_bold, "*", "italic")

    replace_images = split_nodes_image(replace_italic)

    replace_links = split_nodes_link(text_nodes)

    return replace_links

text_to_textnodes([final_result])
