import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertEqual(node.url, "https://example.com")
    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        expected_repr = "TextNode(This is a text node, italic, None)"
        self.assertEqual(repr(node), expected_repr)
    def test_text_type(self):
        node = TextNode("This is a code block", TextType.CODE)
        self.assertEqual(node.text_type, TextType.CODE)
        self.assertNotEqual(node.text_type, TextType.TEXT)
    def test_eq_url_false(self):
        node1 = TextNode("This is a link", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()