import unittest
from block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_blank_lines(self):
        md = """

    # Title

    Some text here

    """
        
        blocks = markdown_to_blocks(md)
        self.assertEqual( blocks, ["# Title", "Some text here"])
           


    def test_lines_with_extra_spaces(self):

        md = "  First line with spaces   \nSecond line  \n\n   Third block with leading spaces    "

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First line with spaces\nSecond line", "Third block with leading spaces"])

    
    def testMultipleBlankLinesBetweenBlocks(self):
        md = "Block one\n\n\nBlock two"
        blocks = markdown_to_blocks(md)
        assert blocks == ["Block one", "Block two"]

    
    def testListsWithIndentation(self):
        md = "-   Item one\n   - Item two\n\nParagraph"
        blocks = markdown_to_blocks(md)
        assert blocks == ["-   Item one\n- Item two", "Paragraph"]


      



if __name__ == "__main__":
    unittest.main()