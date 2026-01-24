import unittest
from viperpress.textnode import TextNode, TextType
import viperpress.generator as generator


class TestTextToHtml(unittest.TestCase):
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


class TestExtractImages(unittest.TestCase):
    def test_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        extracted = generator.extract_markdown_images(text)

        self.assertEqual(
            extracted,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )


class TestExtractLinks(unittest.TestCase):
    def test_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        extracted = generator.extract_markdown_links(text)

        self.assertEqual(
            extracted,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )


class TestSplitter(unittest.TestCase):
    def test_provided(self):
        node = TextNode("This is text with a `code block` word", TextType.Plain)
        new_nodes = generator.split_nodes_delimiter([node], "`", TextType.Code)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("code block", TextType.Code),
                TextNode(" word", TextType.Plain),
            ],
            new_nodes,
        )

    def test_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.Plain)
        new_nodes = generator.split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("bolded", TextType.Bold),
                TextNode(" word", TextType.Plain),
            ],
            new_nodes,
        )

    def test_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.Plain)
        new_nodes = generator.split_nodes_delimiter([node], "_", TextType.Italic)
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.Plain),
                TextNode("italic", TextType.Italic),
                TextNode(" word", TextType.Plain),
            ],
            new_nodes,
        )

    def test_multiple(self):
        node = TextNode(
            "This is text with `multiple code` blocks `within` it.  It `should` pose more of a challenge.",
            TextType.Plain,
        )
        new_nodes = generator.split_nodes_delimiter([node], "`", TextType.Code)
        self.assertEqual(
            [
                TextNode("This is text with ", TextType.Plain),
                TextNode("multiple code", TextType.Code),
                TextNode(" blocks ", TextType.Plain),
                TextNode("within", TextType.Code),
                TextNode(" it.  It ", TextType.Plain),
                TextNode("should", TextType.Code),
                TextNode(" pose more of a challenge.", TextType.Plain),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
