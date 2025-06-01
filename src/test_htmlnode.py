import unittest
from htmlnode import HTMLNode, HTMLNodeType

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, world!", props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), 'class="my-class" id="my-id"')

    def test_props_to_html_false(self):
        node = HTMLNode("div", "testing the props")
        self.assertNotEqual(node.props_to_html(), 'class="my-class" id="my-id"')

    def test_to_html(self):
        node = HTMLNode("div", "Hello, world!", props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.to_html(), '<div class="my-class" id="my-id">Hello, world!</div>')