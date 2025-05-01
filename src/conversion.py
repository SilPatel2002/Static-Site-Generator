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


def extract_markdown_images(text):
   
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return matches


def extract_markdown_links(text):

    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

    return matches