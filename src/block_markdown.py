

def markdown_to_blocks(markdown: str):
 

    blocks = markdown.split("\n\n")

    lines = list(map(lambda block: block.split("\n"), blocks))
    lines = list(map(lambda line: list(map(lambda x: x.strip(), line)), lines))
    lines = list(map(lambda line: list(filter(lambda x: x != "", line)), lines))
    blocks = list(map(lambda block: "\n".join(block), lines))

    blocks = list(filter(lambda block: block != "", blocks))

    return blocks





md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """


markdown_to_blocks(md)