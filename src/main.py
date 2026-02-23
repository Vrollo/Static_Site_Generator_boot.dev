import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from extract_markdown_url import extract_markdown_images, extract_markdown_links

def print_nodes(nodes):
    tab = 4
    print("New nodes:")
    print("[")
    for node in nodes:
        print(f"{tab * " "}{node},")
    print("]")    

def old_test():
    text_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    test = {"href": "https://www.google.com", "target": "_blank"}
    # print(text_node)
    node = HTMLNode("p", "Hello, world!", None, {"class": "primary"})
    # print(node)
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
    # print(leaf_node.to_html())
    # print(leaf_node)

    # node = ParentNode(
    #     "p",
    #     [
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         LeafNode("i", "italic text"),
    #         LeafNode(None, "Normal text"),
    #     ],
    # )

    # print(node.to_html())

    # node = TextNode("This is a text node", TextType.TEXT)
    # text_node = text_node_to_html_node(node)
    # print(text_node.to_html())

    # node = TextNode("This is bold text", TextType.BOLD)
    # bold_node = text_node_to_html_node(node)
    # print(bold_node.to_html())

    # node = TextNode("This is hyperlink", TextType.LINK, "https://www.boot.dev")
    # url_node = text_node_to_html_node(node)
    # print(url_node.to_html())

    # node = TextNode("This is an image", TextType.IMAGE, "image.jpg")
    # image_node = text_node_to_html_node(node)
    # print(image_node.to_html())    

    # node = TextNode("This is text with a `code block` word. This is **bold** text.", TextType.TEXT)
    # # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # node = TextNode("This is **bold**, and this is **bold too**.", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    # print(new_nodes)

    # text = "This is **bold, text"
    # split_text = text.split("**")
    # print(split_text)

    # print_nodes(new_nodes)

    # new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)

    # print_nodes(new_nodes)

    # new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.TEXT)

    # print_nodes(new_nodes)    


    # node = TextNode("This is **bold text**, and this is not. This is *italic* text.", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "**", TextType.TEXT)

    # print_nodes(new_nodes)

    # new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.TEXT)

    # print_nodes(new_nodes)


    # new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.TEXT)

def extract_md():
    # text = "My phone number is 555-555-5555 and my friends number is 555-555-5556"
    # matches = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    # print(matches)

    # text = "I have an (Aprilia) and a (Ducati)"
    # matches = re.findall(r"\((.*?)\)", text)
    # print(matches)

    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    pass

def inline_md_split():
    image_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )

    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev)",
    #     TextType.TEXT,
    # )    

    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) website",
    #     TextType.TEXT,
    # )    


    # node = TextNode(
    #     "[to boot dev](https://www.boot.dev) is the link to the website.",
    #     TextType.TEXT,
    # )    

    # node = TextNode(
    #     "is the link to the website.",
    #     TextType.TEXT,
    # )        

    # new_nodes = split_nodes_link([node])
    # print_nodes(new_nodes)
    new_nodes = split_nodes_image([image_node])

def main():

    node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


    new_nodes = text_to_textnodes(text)

    print_nodes(new_nodes)


if __name__ == "__main__":
    main()