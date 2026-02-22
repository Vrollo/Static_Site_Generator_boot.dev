from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter: str, text_type: TextType):
    new_node_list = []
    code_blocks_text = []
    start_code = -1
    end_code = -1
    # print(f"Old nodes: {old_nodes}")
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)

    # Search for a codeblock ` `
    # start_code = old_nodes[0].text.find(delimiter)
    # end_code = old_nodes[0].text.find(delimiter, start_code + len(delimiter))

    # if end_code < 0:
    #     raise Exception(f"Invalid Markdown syntax, missing closing \"{delimiter}\" delimiter")

    # Also check if a block happens more than once in a text
    # For example: Hello **this is bold**, and the the next work is also **bold**

    # print(f"{start_code} - {end_code}")
    # code_blocks_text.append(old_nodes[0].text[start_code+len(delimiter):end_code])


    print("Searching for other delimiter block")
    start_code = old_nodes[0].text.find(delimiter, end_code + 1)
    if start_code >= 0:
        end_code = old_nodes[0].text.find(delimiter, start_code + len(delimiter))
        if end_code < 0:
            raise Exception(f"Invalid Markdown syntax, missing closing \"{delimiter}\" delimiter")
        else:
            code_blocks_text.append(old_nodes[0].text[start_code+len(delimiter):end_code])
    else:
        end_code = -1

    print("Did we find a 2nd code block?")
    print(f"{start_code} - {end_code}")
    
    print("Delimiter blocks found:")
    for block in code_blocks_text:
        print(block)


    split_nodes = old_nodes[0].text.split(delimiter)
    # print(split_nodes)
    for node in split_nodes:
        if node in code_blocks_text:
            match delimiter:
                case "`":
                    new_node_list.append(TextNode(node, TextType.CODE))
                case "**":
                    new_node_list.append(TextNode(node, TextType.BOLD))
                case "*":
                    new_node_list.append(TextNode(node, TextType.ITALIC))
        else:
            new_node_list.append(TextNode(node, TextType.TEXT))

    # Search for a bold **
    start_bold = float("-inf")

    # print(new_node_list)

    # Search for Italic *


    return new_node_list

