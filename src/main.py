import unittest
from textnode import TextNode
import re
import os
import shutil
from block_markdown import markdown_to_html_node


def main():
    print("HELLO WORLD")


def move_files(list, src, destination):  # Destination will be ./public

    if len(list) == len(os.listdir(src)):  # <-- This is executed the first time.
        if os.path.exists(destination):
            shutil.rmtree(destination)

        os.mkdir(destination)

    if len(list) == 0:  # <-- This stops the recursion.
        return list

    current_file: str = list[0]
    if os.path.isfile(f"{src}/{current_file}"):
        shutil.copy(f"{src}/{current_file}", destination)
    elif os.path.isdir(f"{src}/{current_file}"):
        os.mkdir(f"{destination}/{current_file}")
        sub_directory_list = os.listdir(f"{src}/{current_file}")
        move_files(sub_directory_list, f"{src}/{current_file}", f"{destination}/{current_file}/")

    move_files(list[1:], src, destination)


# static_dir_content = os.listdir("./static")
# move_files(static_dir_content, "./static", "./public")

main()



def extract_title(markdown):
    h1 = re.findall("(?<!#)\# \w+", markdown)
    if len(h1) == 0:
        raise Exception("No <h1> found!")
    return h1[0].strip("# ")

# ~/Documents/GitHub/static_site_generator/content/index.md

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = open(from_path).read()
    template_content = open(template_path).read()
    html_content = markdown_to_html_node(markdown_content)

    print(html_content.to_html())

    # print(markdown_content)
    # print("NEXT")
    # print(template_content)
    # print("NEXT")
    # print(html_content)

generate_page("./content/index.md", "./template.html", "./full_test")