import unittest

from conversion import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestTextNodetoHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        html_node1 = text_node_to_html_node(node)
        self.assertEqual(html_node1.tag, "a")
        self.assertEqual(html_node1.value, "This is a text node")
        self.assertEqual(html_node1.props, {"href": "www.google.com"})

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "www.google.com")
        html_node1 = text_node_to_html_node(node)
        self.assertEqual(html_node1.tag, "img")
        self.assertEqual(html_node1.value, "")
        self.assertEqual(html_node1.props, {"src": "www.google.com", "alt": "This is a text node"})


    def test_invalid_type(self):

        with self.assertRaises(Exception):
     
            class MockTextNode:
                def __init__(self):
                    self.text = "test"
                    self.text_type = "invalid_type"
            
            node = MockTextNode()
            text_node_to_html_node(node)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)




if __name__ == "__main__":
    unittest.main()