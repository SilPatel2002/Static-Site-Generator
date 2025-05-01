from conversion import extract_markdown_images
import unittest


class TestExtractMarkdownImages(unittest.TestCase):

    def test(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        text = "Image 1: ![dog](https://example.com/dog.png) and Image 2: ![bird](https://example.com/bird.jpg)"
        result = extract_markdown_images(text)
        expected = [("dog", "https://example.com/dog.png"), ("bird", "https://example.com/bird.jpg")]
        assert result == expected


    def test_mixed_content(self):
        text = "Here's a [link](https://example.com) and an ![image](https://example.com/pic.jpg)"
  
        image_result = extract_markdown_images(text)
  
        assert image_result == [("image", "https://example.com/pic.jpg")]




if __name__ == "__main__":
    unittest.main()