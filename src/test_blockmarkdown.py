import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class ClassBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        md = """     
#This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "#This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks3(self):
        md = """
#This is a heading 1

##This is a heading 2

A code block
`
def main():
    return 0
`



Lots of empty lines above:

1 Item one
2 Item two
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "#This is a heading 1",
                "##This is a heading 2",
                "A code block\n`\ndef main():\n    return 0\n`",
                "Lots of empty lines above:",
                "1 Item one\n2 Item two",
            ],
        )        

    def test_heading_block(self):
        text = "###### This is a heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_code_block(self):
        text = """```
This is a 
multiline
code block
```"""
        self.assertEqual(block_to_block_type(text), BlockType.CODE)

    def test_quote_block(self):
        text = """> This is a quote
> Quote this
> End this"""
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_unordered_list(self):
        text = """- This is
- an unordered
- list"""
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        text = """1. This is
2. an unordered
3. list
4. and more item"""
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)

    def test_paragraph_block1(self):
        text = """1. This is
2.an unordered
3. list
4. and more item"""
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_paragraph_block2(self):
        text = "This is a simple text"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

