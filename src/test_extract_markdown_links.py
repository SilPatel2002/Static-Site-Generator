from conversion import extract_markdown_links
import unittest


class TestExtractMarkdownLinks(unittest.TestCase):
    
    def test(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")] )
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


    def test_multiple_links(self):
        text = "Visit [site one](https://example1.com) or [site two](https://example2.com)"
        result = extract_markdown_links(text)
        expected = [("site one", "https://example1.com"), ("site two", "https://example2.com")]
        assert result == expected


    def test_mixed_content(self):
        text = "Here's a [link](https://example.com) and an ![image](https://example.com/pic.jpg)"
        link_result = extract_markdown_links(text)
        assert link_result == [("link", "https://example.com")]


if __name__ == "__main__":
    unittest.main()