import unittest

from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = "[TextNode(This is text with a , TextType.TEXT, None), TextNode(code block, TextType.CODE, None), TextNode( word, TextType.TEXT, None)]"
        self.assertEqual(repr(new_nodes), expected)

    def test_bold(self):
        node = TextNode("This next word is **bold**, and then continues like normal", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = "[TextNode(This next word is , TextType.TEXT, None), TextNode(bold, TextType.BOLD, None), TextNode(, and then continues like normal, TextType.TEXT, None)]"
        self.assertEqual(repr(new_nodes), expected)       

    def test_italic(self):
        node = TextNode("A word in *Italic*.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = "[TextNode(A word in , TextType.TEXT, None), TextNode(Italic, TextType.ITALIC, None), TextNode(., TextType.TEXT, None)]"
        self.assertEqual(repr(new_nodes), expected)  

    def test_multiple_same(self):
        node = TextNode("This is **bold**, and this is **bold too**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = "[TextNode(This is , TextType.TEXT, None), TextNode(bold, TextType.BOLD, None), TextNode(, and this is , TextType.TEXT, None), TextNode(bold too, TextType.BOLD, None), TextNode(., TextType.TEXT, None)]"
        self.assertEqual(repr(new_nodes), expected)  

    def test_mixed(self):
        node = TextNode("This is **bold**, and this is *italic* text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        expected = "[TextNode(This is , TextType.TEXT, None), TextNode(bold, TextType.BOLD, None), TextNode(, and this is , TextType.TEXT, None), TextNode(italic, TextType.ITALIC, None), TextNode( text., TextType.TEXT, None)]"
        self.assertEqual(repr(new_nodes), expected)  

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT, None),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ], 
            new_nodes,
        )