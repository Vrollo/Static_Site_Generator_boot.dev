from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import TextType, TextNode, text_node_to_html_node

def count_consecutive_char(text, search_char) -> int:
    count = 0
    for char in text:
        if char == search_char:
            count += 1
        else:
            break
    return count

def text_to_children(text):
    pass

def block_node_to_html_node(text: str, block_type: BlockType):
    node: HTMLNode = None
    print(f"\n{block_type} - {text}\n")
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
                c_node.append(LeafNode("li", word[2:], None))
            node = ParentNode("ul", c_node, None)
        case BlockType.OLIST:
            c_node = []
            for word in text.split("\n"):
                c_node.append(LeafNode("li", word[3:], None))
            node = ParentNode("ol", c_node, None)
    return node    


def markdown_to_html_node(markdown):


    md_blocks = markdown_to_blocks(markdown)
    nodes = []
    md_text_blocks = []

    # There will be a ParentNode with div created where all the blocks reside in

    for block in md_blocks:
        # print(block)
        if len(md_blocks) > 1:
            # Still need to implement this part

            # inline_md_split returns a list of textnodes
            # convert the textnodes to html with text_node_to_html_node which returns a LeafNode
            # each LeafeNode node will then be appended to nodes[]
            
            print("This block contains child nodes")
        else:
            print("This main block should be a LeafNode and not a ParentNode")
            nodes.append(block_node_to_html_node(block, block_to_block_type(block)))

        # print(block)
        # print(block_to_block_type(block))
        # md_text_blocks.append(text_to_textnodes(block))
    parent_node = ParentNode("div", nodes, None)
    print(parent_node.to_html())

    # for block in md_text_blocks:
    #     for b in block:
    #         print(text_node_to_html_node(b).to_html())

    # for node in nodes:
    #     print(node.to_html())

    pass



# 1. Convert the Markdown text into blocks using markdown_to_blocks
# 2. For each block you can then determine what kind of BlockType it is
#    Most of this will be parent nodes, but some of them leaf nodes if they don't have children
# 3. Convert the MarkDown blocks into smaller TextNode  Blocks 
# 4. Each TextNode can then be converted to a HTMLNode
