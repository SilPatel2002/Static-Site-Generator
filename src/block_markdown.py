from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"









def markdown_to_blocks(markdown: str):
 

    blocks = markdown.split("\n\n")

    lines = list(map(lambda block: block.split("\n"), blocks))
    lines = list(map(lambda line: list(map(lambda x: x.strip(), line)), lines))
    lines = list(map(lambda line: list(filter(lambda x: x != "", line)), lines))
    blocks = list(map(lambda block: "\n".join(block), lines))

    blocks = list(filter(lambda block: block != "", blocks))

    return blocks



def block_to_block_type(block):

    if re.match(r'^#{1,6} ', block):
        return BlockType.HEADING
    
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    lines = block.split("\n")

    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(re.match(r'^\d+\. ', line) for line in lines):
        try:

            numbers = [int(re.match(r'^(\d+)\.', line).group(1)) for line in lines]
            expected = list(range(1, len(lines) + 1))
            if numbers == expected:
                return BlockType.ORDERED_LIST
            
        except(AttributeError, ValueError):
            pass
            
    
    return BlockType.PARAGRAPH
