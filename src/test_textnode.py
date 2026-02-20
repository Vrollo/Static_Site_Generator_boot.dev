import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # def test_eq2(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.ITALIC)
    #     self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        self.assertEqual(node, node2)        

    # def test_neq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node number 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "<b>This is bold text</b>")

    def test_text(self):
        node = TextNode("This is hyperlink", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">This is hyperlink</a>')

    def test_text(self):
        node = node = TextNode("This is an image", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), '<img src="image.jpg" alt="This is an image">')          

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )              

if __name__ == "__main__":
    unittest.main()