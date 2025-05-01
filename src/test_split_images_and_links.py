from conversion import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import unittest



class TestSplitImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    
    def test_split_image_multiple(self):
        node = TextNode(
            "![first](https://example.com/1.png) and ![second](https://example.com/2.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("first", TextType.IMAGE, "https://example.com/1.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.IMAGE, "https://example.com/2.png")
        ], new_nodes)



    def test_split_image_no_images(self):
        node = TextNode("Just plain text, no images here", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)  # Original node should be returned



    def test_split_image_non_text_node(self):
        node = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)  # Non-TEXT nodes should be preserved


    def test_split_image_multiple_nodes(self):
        nodes = [
            TextNode("Text with ![img](https://example.com/img.png)", TextType.TEXT),
            TextNode("Bold", TextType.BOLD)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(new_nodes,[
            TextNode("Text with ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://example.com/img.png"),
            TextNode("Bold", TextType.BOLD)
        ])







class TestSplitLinks(unittest.TestCase):
    def test_split_link_basic(self):
        node = TextNode("This is a [link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ], new_nodes)



    def test_split_link_multiple(self):
        node = TextNode(
            "[first](https://example.com/1) and [second](https://example.com/2)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("first", TextType.LINK, "https://example.com/1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.LINK, "https://example.com/2")
        ], new_nodes)




    def test_split_link_no_links(self):
        node = TextNode("Just plain text, no links here", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)  # Original node should be returned




    def test_split_link_non_text_node(self):
        node = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)  # Non-TEXT nodes should be preserved


    def test_split_link_multiple_nodes(self):
        nodes = [
            TextNode("Text with [link](https://example.com)", TextType.TEXT),
            TextNode("Bold", TextType.BOLD)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(new_nodes, [
            TextNode("Text with ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode("Bold", TextType.BOLD)
        ])





if __name__ == "__main__":
    unittest.main()