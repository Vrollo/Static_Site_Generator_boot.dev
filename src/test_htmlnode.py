import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        prop = {
            "href": "www.boot.dev", 
            "target": "_blank"
        }
        node = HTMLNode("p", "This is a paragraph", None, prop)
        expected = ' href="www.boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        prop1 = {
            "img src": "./some_img2.png", 
            "alt": "image description", 
            "height": "200"
        }
        prop2 = {
            "href": "www.boot.dev", 
            "target": "_blank"
        }        
        node1 = HTMLNode("h1", "This is node1")
        node2 = HTMLNode("p", "This is a paragraph")
        children_nodes = [node1, node2]
        node3 = HTMLNode("div", "This is a node with children", children_nodes, prop1)
        node4 = HTMLNode("h3", "Node with empty prop dict", None, prop2)
        #
        self.assertEqual(node1.tag, "h1")
        self.assertEqual(node1.value, "This is node1")
        self.assertEqual(node1.children, None)
        self.assertEqual(node1.props, None)

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", None, {"class": "primary"})
        # This checks if your __repr__ output matches what you expect
        self.assertEqual(
            repr(node), 
            "HTMLNode(p, Hello, world!, children: None, {'class': 'primary'})"
        )        

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This value has no tag!!!")
        self.assertEqual(node.to_html(), "This value has no tag!!!")

    def test_leaf_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            repr(node),
            "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, child_node)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_children(self):
        parent_node = ParentNode("ol", None)
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
    unittest.main()