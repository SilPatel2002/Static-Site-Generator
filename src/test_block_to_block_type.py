import unittest
from block_markdown import BlockType, block_to_block_type


class TestParagraph(unittest.TestCase):
    def test_simple(self):
        # Simple paragraph
        assert block_to_block_type("This is a simple paragraph.") == BlockType.PARAGRAPH


    def test_multiple(self):
        # Multi-line paragraph
        assert block_to_block_type("This is a paragraph.\nWith multiple lines.") == BlockType.PARAGRAPH



class TestHeading(unittest.TestCase):
    
    def test_simple(self):
                # H1 heading
        assert block_to_block_type("# This is a heading") == BlockType.HEADING

        # H3 heading
        assert block_to_block_type("### This is a smaller heading") == BlockType.HEADING

        # H6 heading
        assert block_to_block_type("###### This is the smallest heading") == BlockType.HEADING

        # Not a heading (no space after #)
        assert block_to_block_type("#This is not a heading") == BlockType.PARAGRAPH




class TestCode(unittest.TestCase):
    def test(self):
        # Simple code block
        assert block_to_block_type("```\ncode goes here\n```") == BlockType.CODE

        # Code block with language specified
        assert block_to_block_type("```python\ndef hello():\n    print('Hello')\n```") == BlockType.CODE

        # Not a code block (only opening backticks)
        assert block_to_block_type("```\nThis is not a complete code block") == BlockType.PARAGRAPH



class TestQuote(unittest.TestCase):
    def test(self):
        # Simple quote
        assert block_to_block_type(">This is a quote") == BlockType.QUOTE

        # Multi-line quote
        assert block_to_block_type(">This is a quote\n>With multiple lines") == BlockType.QUOTE

        # Not a quote (second line doesn't start with >)
        assert block_to_block_type(">This is a quote\nBut this isn't") == BlockType.PARAGRAPH



class TestUnorderedList(unittest.TestCase):
    def test(self):
        # Simple unordered list
        assert block_to_block_type("- Item 1\n- Item 2\n- Item 3") == BlockType.UNORDERED_LIST

class TestOrderedList(unittest.TestCase):
    def test(self):
        # Simple ordered list
        assert block_to_block_type("1. First item\n2. Second item\n3. Third item") == BlockType.ORDERED_LIST

        # Ordered list with more items
        assert block_to_block_type("1. Item one\n2. Item two\n3. Item three\n4. Item four\n5. Item five") == BlockType.ORDERED_LIST

        # Not an ordered list (numbers don't start at 1)
        assert block_to_block_type("2. Second item\n3. Third item\n4. Fourth item") == BlockType.PARAGRAPH

        # Not an ordered list (numbers don't increment correctly)
        assert block_to_block_type("1. First item\n3. Third item\n4. Fourth item") == BlockType.PARAGRAPH

        # Not an ordered list (mixed with unordered list items)
        assert block_to_block_type("1. First item\n- Bullet point\n3. Third item") == BlockType.PARAGRAPH










if __name__ == "__main__":
    unittest.main()