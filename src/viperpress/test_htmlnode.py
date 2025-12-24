import unittest

from viperpress.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_single_props(self):
        node = HTMLNode(props={"target": "_blank"})

        self.assertEqual(node.props_to_html(), ' target="_blank"')

    def test_multi_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_repr_simple(self):
        node = HTMLNode(tag="h1", value="My title")

        self.assertEqual(repr(node), "<h1>My title</h1>")

    def test_repr_complex(self):
        node = HTMLNode(
            tag="a",
            value="My link",
            props={"href": "https://www.google.com", "target": "_blank"},
        )

        result = '<a href="https://www.google.com" target="_blank">My link</a>'

        self.assertEqual(repr(node), result)

    def test_repr_children(self):
        child = HTMLNode(tag="h1", value="My link title")

        parent = HTMLNode(tag="a", children=[child])

        result = "<a><h1>My link title</h1></a>"

        self.assertEqual(repr(parent), result)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


class TestParentNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
