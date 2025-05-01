import unittest

from conversion import text_node_to_html_node, split_nodes_delimiter
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode



class TestSplitNodesDelimeter(unittest.TestCase):
    def test_text_with_no_delimeters(self):
        node = TextNode("This is a test", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(node_list, [node])


    def test_text_single_pair_delimeters(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                        TextNode("This is text with a ", TextType.TEXT),
                                        TextNode("code block", TextType.CODE),
                                        TextNode(" word", TextType.TEXT),
                                    ])
        


    def test_text_multiple_pair_delimeters(self):
        node = TextNode("This is **text** with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ])

    def test_text_unmatched_delimeters(self):
        
        with self.assertRaises(Exception):
            node = TextNode("This is a **test node", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)


    def test_text_different_delimeters(self):
        node = TextNode("This is a text node with **bold** and _italics_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is a text node with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
        ])







if __name__ == "__main__":
    unittest.main()