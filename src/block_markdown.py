from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    temp_blocks = markdown.split("\n\n")

    for block in temp_blocks:
        if block != "":
            blocks.append(block.strip())

    return blocks

def block_to_block_type(words) -> BlockType:
    # Don't need to think about '\n' at the beginning of the line as these are stripped with markdown_to_blocks

    # Heading block
    if words.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    # Multiline Code block
    if words.startswith("```") and words.endswith("```"):
        return BlockType.CODE

    # Quote block
    valid_quote_block = True
    for word in words.split("\n"):
        if not word.startswith(">"):
            valid_quote_block = False
    if valid_quote_block:
        return BlockType.QUOTE

    # Unordered list
    valid_unordered_list = True
    for word in words.split("\n"):
        if not word.startswith("- "):
            valid_unordered_list = False
    if valid_unordered_list:
        return BlockType.UNORDERED_LIST

    # ordered list
    valid_ordered_list = True
    index = 1
    for word in words.split("\n"):
        if not word.startswith(f"{index}. "):
            valid_ordered_list = False
        index += 1
    if valid_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

    pass