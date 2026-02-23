from textnode import TextNode, TextType
from extract_markdown_url import extract_markdown_images, extract_markdown_links

def search_delimiter_blocks(node, delimiter):
    delimiter_block_list = []
    start_code = -1
    end_code = -1
    search = True

    while search:
        start_code = node.text.find(delimiter, end_code + 1)
        if start_code >= 0:
            end_code = node.text.find(delimiter, start_code + len(delimiter))
            if end_code < 0:
                raise Exception(f"Invalid Markdown syntax, missing closing \"{delimiter}\" delimiter")
            else:
                delimiter_block_list.append(node.text[start_code+len(delimiter):end_code])
        else:
            end_code = -1   
            search = False     

    return delimiter_block_list

def split_nodes_delimiter(old_nodes, delimiter: str, text_type: TextType):
    new_node_list = []
    code_blocks_text = []

    for node in old_nodes:
        start_code = -1
        end_code = -1
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
        else:
            code_blocks_text = search_delimiter_blocks(node, delimiter)

            split_nodes = node.text.split(delimiter)
            for n in split_nodes:
                if n in code_blocks_text:
                    new_node_list.append(TextNode(n, text_type))
                else:
                    new_node_list.append(TextNode(n, TextType.TEXT))

    return new_node_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



def text_to_textnodes(text):
    new_nodes = []

    new_nodes.append(TextNode(text, TextType.TEXT))

    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_image(new_nodes)

    # node = TextNode(text, TextType.TEXT)
    # node1 = split_nodes_delimiter([node], "**", TextType.BOLD)
    # node2 = split_nodes_delimiter(node1, "*", TextType.ITALIC)
    # node3 = split_nodes_delimiter(node2, "`", TextType.CODE)
    # node4 = split_nodes_link(node3)
    # node5 = split_nodes_image(node4)
    
    # new_nodes.append(node1)
    # new_nodes.append(node2)
    # new_nodes.append(node3)
    # new_nodes.append(node4)
    # new_nodes.append(node5)


    return new_nodes
    

