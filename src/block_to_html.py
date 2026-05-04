from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

def count_consecutive_char(text, search_char) -> int:
    count = 0
    for char in text:
        if char == search_char:
            count += 1
        else:
            break
    return count

def extract_title(markdown: str) -> str:
    # Title should always but the 1st markdown block
    md_blocks = markdown_to_blocks(markdown)
    block = md_blocks[0]
    title = ""
    count = count_consecutive_char(block, "#")
    if (block_to_block_type(block) == BlockType.HEADING) and (count == 1):
        title = block.replace("#", "").strip()
    else:
        raise Exception("Invalid title: no '# ' heading found in the first MD block")
    return title

def block_node_to_html_node(text: str, block_type: BlockType) -> HTMLNode:
    node: HTMLNode = None
    # print(f"\n{block_type} - {text}\n")
    match block_type:
        case BlockType.PARAGRAPH:
            node = LeafNode("p", text, None)
        case BlockType.HEADING:
            s = text.replace("#", "").strip()
            count = count_consecutive_char(text, "#")
            if count <= 6:
                node = LeafNode(f"h{count}", s, None)
        case BlockType.CODE:
            s = text.replace("`", "").strip()
            c_node = []
            # Can use text_node_to_html_node here to create the leafnode
            c_node.append(LeafNode("code", s, None))
            node = ParentNode("pre", c_node, None)
        case BlockType.QUOTE:
            s = text.replace(">", "").strip()
            node = LeafNode("blockquote", s, None)
        case BlockType.ULIST:
            # text = text.replace("- ", "")
            c_node = []
            for word in text.split("\n"):
                # TODO the text needs to be converted to html too. The example contains an italic
                inter_str = ""
                text_nodes = text_to_textnodes(word[2:])
                for node in text_nodes:
                    child_node = text_node_to_html_node(node)
                    inter_str += child_node.to_html()
                c_node.append(LeafNode("li", inter_str, None))
            node = ParentNode("ul", c_node, None)
        case BlockType.OLIST:
            c_node = []
            for word in text.split("\n"):
                # TODO the text needs to be converted to html too. The example contains an italic
                inter_str = ""
                text_nodes = text_to_textnodes(word[3:])
                for node in text_nodes:
                    child_node = text_node_to_html_node(node)
                    inter_str += child_node.to_html()
                c_node.append(LeafNode("li", inter_str, None))
            node = ParentNode("ol", c_node, None)
    return node    


def markdown_to_html_node(markdown: str) -> HTMLNode:


    md_blocks = markdown_to_blocks(markdown)
    nodes = []
    # md_text_blocks = []

    # There will be a ParentNode with div created where all the blocks reside in

    for block in md_blocks:
        # print(block)
        if len(md_blocks) > 1:
            # everything was theated as a PARAGRAPH added a condition for now
            # print(block_to_block_type(block))
            if (block_to_block_type(block)) != BlockType.PARAGRAPH:
                nodes.append(block_node_to_html_node(block, block_to_block_type(block)))
                continue    

            # When there are more blocks, this means you have a paragraph with child nodes
            # child nodes should be though of bold, italic, text image et

            # inline_md_split returns a list of strings
            # convert the list of strings to TextNode, text_to_textnodes returns a list of TextNode

            # replace \n as this seems to be the case in the example test case from boot.dev
            
            # TODO - This part has to be rewritten to call the helper function block_node_to_html_node for paragraph
            # TODO - Although it might be correct and the below part needs to be moved into the helper function

            inter_nodes = []    # intermediate node that can be added to nodes[] as a child, as it needs to be wrapped with <p></p>
            text_nodes = text_to_textnodes(block.replace("\n", " "))
            for text_node in text_nodes:
                child_node = text_node_to_html_node(text_node)
                inter_nodes.append(child_node)

            # Each block should be wrapped in a paragraph node, which is a ParentNode
            paragraph_node = ParentNode("p", inter_nodes, None)
            nodes.append(paragraph_node)
        else:
            # print("This main block should be a LeafNode and not a ParentNode")
            nodes.append(block_node_to_html_node(block, block_to_block_type(block)))

        # print(block)
        # print(block_to_block_type(block))
        # md_text_blocks.append(text_to_textnodes(block))

    return ParentNode("div", nodes, None)
    # return parent_node

    # print(parent_node.to_html())

    # for block in md_text_blocks:
    #     for b in block:
    #         print(text_node_to_html_node(b).to_html())

    # for node in nodes:
    #     print(node.to_html())




# 1. Convert the Markdown text into blocks using markdown_to_blocks
# 2. For each block you can then determine what kind of BlockType it is
#    Most of this will be parent nodes, but some of them leaf nodes if they don't have children
# 3. Convert the MarkDown blocks into smaller TextNode  Blocks 
# 4. Each TextNode can then be converted to a HTMLNode
