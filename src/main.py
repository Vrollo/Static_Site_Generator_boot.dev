from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitnodes import split_nodes_delimiter

def print_nodes(nodes):
    tab = 4
    print("New nodes:")
    print("[")
    for node in nodes:
        print(f"{tab * " "}{node},")
    print("]")    

def main():
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

    # node = TextNode("This is text with a `code block` word, and here is `another code block`. This is **bold** text.", TextType.TEXT)

    node = TextNode("This is **bold text**, and this is not. This is *italic* text.", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.TEXT)

    print_nodes(new_nodes)

    # new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.TEXT)

    # print_nodes(new_nodes)


    # new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.TEXT)


if __name__ == "__main__":
    main()