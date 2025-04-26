import unittest
from htmlnode import HTMLNode

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
  


if __name__ == "__main__":
    unittest.main()