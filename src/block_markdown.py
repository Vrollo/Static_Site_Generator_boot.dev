import typing

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> typing.List[str]:
    # This function returns a list of strings
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
    valid_ULIST = True
    for word in words.split("\n"):
        if not word.startswith("- "):
            valid_ULIST = False
    if valid_ULIST:
        return BlockType.ULIST

    # ordered list
    valid_OLIST = True
    index = 1
    for word in words.split("\n"):
        if not word.startswith(f"{index}. "):
            valid_OLIST = False
        index += 1
    if valid_OLIST:
        return BlockType.OLIST

    return BlockType.PARAGRAPH

    pass