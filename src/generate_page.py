import html
import os
from platform import node
from tempfile import template
from turtle import title
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open("src/template.html", "r")
    template_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    htlm = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{title}}", html.escape(title))
    template = template.replace("{{content}}", htlm)

    dest_dir_path = os.path.dirname(dest_path)  
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    to_file = open(dest_path, "w")
    to_file.write(template) 

def extract_title(markdown_content):
    lines = markdown_content.splitlines()
    for line in lines:
        if line.startswith('# '):
            return line[2:]
    return "Untitled"
