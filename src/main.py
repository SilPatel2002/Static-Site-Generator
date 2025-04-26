from textnode import *
from htmlnode import HTMLNode

def main():
    x = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(x)

    y = HTMLNode("p", "awesome")
    print(y)



main()