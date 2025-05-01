import unittest
from conversion import text_to_textnodes
from textnode import TextNode, TextType



class TestTextToTextnodes(unittest.TestCase):

    def test(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)

        assert new_nodes == [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
        


    def test_text_to_textnodes(self):
        # Test case 1: Basic markdown with all elements
        text1 = "This is **bold** and _italic_ with `code` and a ![image](https://example.com/img.jpg) and a [link](https://example.com)"
        nodes1 = text_to_textnodes(text1)
        # Verify the length and content of nodes1
        assert nodes1 == [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ]
        
        # Test case 2: Multiple instances of the same markdown element
        text2 = "**Bold1** normal **Bold2** normal **Bold3**"
        nodes2 = text_to_textnodes(text2)
        # Verify nodes2

        assert nodes2 == [
            TextNode("Bold1", TextType.BOLD),
            TextNode(" normal ", TextType.TEXT),
            TextNode("Bold2", TextType.BOLD),
            TextNode(" normal ", TextType.TEXT),
            TextNode("Bold3", TextType.BOLD)
        ]
        
        # Test case 3: No markdown elements
        text3 = "Plain text without any markdown"
        nodes3 = text_to_textnodes(text3)
        # Should be a single TextNode with TextType.TEXT

        assert nodes3 == [
            TextNode("Plain text without any markdown", TextType.TEXT)
        ]
        
        # Test case 4: Empty string
        text4 = ""
        nodes4 = text_to_textnodes(text4)
        # Should be a single empty TextNode with TextType.TEXT

        assert nodes4 == [
            TextNode("", TextType.TEXT)
        ]
        
        # Test case 5: Adjacent markdown elements
        text5 = "**Bold**_Italic_`Code`"
        nodes5 = text_to_textnodes(text5)
        # Verify nodes5

        assert nodes5 == [
            TextNode("Bold", TextType.BOLD),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code", TextType.CODE)
        ]
        





if __name__ == "__main__":
    unittest.main()