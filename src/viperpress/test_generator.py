import unittest
from viperpress.textnode import TextNode, TextType
import viperpress.generator as generator


class TestGenerator(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.Plain)
        html_node = generator.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is alt text", TextType.Image, "/images/example.png")
        html_node = generator.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "/images/example.png")
        self.assertEqual(html_node.props["alt"], "This is alt text")

    def test_link(self):
        node = TextNode(
            "This link goes to google", TextType.Link, "https://www.google.com"
        )
        html_node = generator.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This link goes to google")
        self.assertEqual(html_node.props["href"], "https://www.google.com")


if __name__ == "__main__":
    unittest.main()
