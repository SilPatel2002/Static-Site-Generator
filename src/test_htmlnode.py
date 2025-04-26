import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props = {"href": "https://example.com"})
        result = node.props_to_html()

        self.assertEqual(result, ' href="https://example.com"')

        
    def test_props_is_None(self):
        node2 = HTMLNode()
        result = node2.props_to_html()
        self.assertEqual(result, "")

    def test_multiple_props(self):
        node = HTMLNode(props={"class": "button", "id": "submit", "disabled": True})
        result = node.props_to_html()
        self.assertEqual(result, ' class="button" id="submit" disabled="True"')


        #===================================TESTING LEAF NODES===========================================


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        result = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(result, "<p>This is a paragraph of text.</p>")
        

    def test_to_html_with_props(self):
       result = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
       self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')

    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    #===================================TESTING PARENT NODES===========================================

  


if __name__ == "__main__":
    unittest.main()