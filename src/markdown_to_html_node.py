from block_markdown import block_to_block_type, markdown_to_blocks, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from conversion import *



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = list(map(text_node_to_html_node, text_nodes))
    return html_nodes

def create_paragraph_node(block):
    new_node = ParentNode("p", [])
    block = block.replace("\n", " ")
    new_node.children = text_to_children(block)
    return new_node

def create_header_node(block):
    #count the number of # at the beginning of block
    count = 0
    for char in block:
        if char == '#':
            count += 1
        else:
            break

    # remove the # characters and any leading/trailing whitespace
    content = block[count:].strip()


    new_node = ParentNode(f"h{count}", [])
    new_node.children = text_to_children(content)
    return new_node

def create_code_node(block):
    # Remove the opening and closing ``` lines
    lines = block.split("\n")

    # Filter out the first and last lines if they contain ```
    if lines[0].strip() == "```":
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]

    


    # Join the remaining lines back together
    content = "\n".join(lines)
    
    #find the last occurance of ```
    index = block.rfind("```", 0, len(block))

    if block[index - 1] == "\n":
        content += "\n"

    #create a pre node with a code node as its child
    pre_node = ParentNode("pre", [])
    code_node = ParentNode("code", [])

    text_node = TextNode(content, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)

    code_node.children = [html_node]
    pre_node.children = [code_node]
    return pre_node

def create_quote_node(block):
    # Process each line to remove the '>' character
    lines = block.split("\n")
    processed_lines = []
    
    for line in lines:
        # Remove the '>' character and any single space after it
        if line.startswith(">"):
            line = line[1:]
            if line.startswith(" "):
                line = line[1:]
        processed_lines.append(line)
    
    # Join the processed lines back together
    content = "\n".join(processed_lines)
    
    # Create the blockquote node
    quote_node = ParentNode("blockquote", [])
    
    # Process inline markdown and add as children
    quote_node.children = text_to_children(content)
    
    return quote_node

def create_ordered_list_node(block):
    # Split the block into lines to process each list item
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Find where the actual content starts (after "X. ")
        # This looks for digits followed by a period and space
        content_start = 0
        for i, char in enumerate(line):
            if char.isdigit():
                continue
            elif char == "." and i + 1 < len(line) and line[i + 1] == " ":
                content_start = i + 2  # Skip past the digit(s), period, and space
                break
            else:
                break
                
        # Extract the content and process inline markdown
        if content_start > 0:
            item_content = line[content_start:]
            list_item = ParentNode("li", [])
            list_item.children = text_to_children(item_content)
            list_items.append(list_item)
    
    # Create the ordered list node with all item nodes as children
    ol_node = ParentNode("ol", list_items)
    
    return ol_node

def create_unordered_list_node(block):
    # Split the block into lines to process each list item
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Find where the actual content starts (after "* " or "- " or "+ ")
        content_start = 0
        if line.startswith("* ") or line.startswith("- ") or line.startswith("+ "):
            content_start = 2  # Skip past the marker and space
            
        # Extract the content and process inline markdown
        if content_start > 0:
            item_content = line[content_start:]
            list_item = ParentNode("li", [])
            list_item.children = text_to_children(item_content)
            list_items.append(list_item)
    
    # Create the unordered list node with all item nodes as children
    ul_node = ParentNode("ul", list_items)
    
    return ul_node


def markdown_to_html_node(markdown):
    #step 1 split the markdown into blocks

    blocks = markdown_to_blocks(markdown)

    # create the parent node
    parent_node = ParentNode("div", [])

    #step 2 loop over each block

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block_node = create_paragraph_node(block)
        elif block_type == BlockType.HEADING:
            block_node = create_header_node(block)
        elif block_type == BlockType.CODE:
            block_node = create_code_node(block)
        elif block_type == BlockType.QUOTE:
            block_node = create_quote_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            block_node = create_unordered_list_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            block_node = create_ordered_list_node(block)
        else:
            raise Exception("Invalid Block Type")
        # add the block node to the parent node
        parent_node.children.append(block_node)
   

    return parent_node