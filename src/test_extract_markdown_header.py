import unittest
from conversion import extract_markdown_header

class TestExtractTitle(unittest.TestCase):

    def test(self):

        maker = '''
                    # Tolkien Fan Club

                    ![JRR Tolkien sitting](/images/tolkien.png)

                    Here's the deal, **I like Tolkien**.

                    > "I am in fact a Hobbit in all but size."
                    >
                    > -- J.R.R. Tolkien

                    ## Blog posts

                    - [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
                    - [Why Tom Bombadil Was a Mistake](/blog/tom)
                    - [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
                    '''
        result = extract_markdown_header(maker)
        assert result == "Tolkien Fan Club"



if __name__ == "__main__":
    unittest.main()