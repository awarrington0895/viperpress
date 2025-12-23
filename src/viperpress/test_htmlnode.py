import unittest

from viperpress.htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
