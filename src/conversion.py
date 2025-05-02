from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

def text_node_to_html_node(text_node: TextNode):

    match text_node.text_type:
        
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)

        case (TextType.BOLD):
            return LeafNode("b", text_node.text)

        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)

        case (TextType.CODE):
            return LeafNode("code", text_node.text)

        case (TextType.LINK):
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case (TextType.IMAGE):
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case default:
            raise Exception("Invalid Text Type")
        

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
        result_nodes = []
        
        # If no delimiter in text, keep the node as is
        if delimiter not in text:
            result_nodes.append(old_node)
            new_nodes.extend(result_nodes)
            continue
        
        # Process the text while delimiters exist
        while delimiter in text:
            # Split at first delimiter
            before, rest = text.split(delimiter, 1)
            
            # Look for closing delimiter
            if delimiter not in rest:
                raise Exception("Invalid Markdown syntax: missing closing delimiter")
                
            # Split at closing delimiter
            content, after = rest.split(delimiter, 1)
            
            # Add nodes for this split
            if before:
                result_nodes.append(TextNode(before, TextType.TEXT))
            result_nodes.append(TextNode(content, text_type))
            
            # Continue with remaining text
            text = after
        
        # Add any remaining text
        if text:
            result_nodes.append(TextNode(text, TextType.TEXT))
            
        new_nodes.extend(result_nodes)
    
    return new_nodes


def extract_markdown_header(text):

    lines = text.split("\n")

    for line in lines:
        if line.strip().startswith('# '):
            line = line.split("# ", 1)
            return line[1].strip()
        
    
    raise Exception("Markdown has no header")


def extract_markdown_images(text):
   
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return matches


def extract_markdown_links(text):

    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_images(text)
        result_nodes = []

        if not matches:
            new_nodes.append(old_node)
            continue

        for match in matches:
            image_alt, image_link = match
            before, after = text.split(f"![{image_alt}]({image_link})", 1)

            if before:
                result_nodes.append(TextNode(before, TextType.TEXT))
            result_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            text = after

        if text:
            result_nodes.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(result_nodes)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_links(text)
        result_nodes = []

        if not matches:
            new_nodes.append(old_node)
            continue

        for match in matches:
            link_text, link_url = match
            before, after = text.split(f"[{link_text}]({link_url})", 1)

            if before:
                result_nodes.append(TextNode(before, TextType.TEXT))
            result_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            text = after

        if text:
            result_nodes.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(result_nodes)

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes



