import unittest

from viperpress.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Text", TextType.Code)
        node2 = TextNode("Other text", TextType.Code)

        self.assertNotEqual(node, node2)

    def test_different_type(self):
        node = TextNode("Text", TextType.Code)
        node2 = TextNode("Text", TextType.Italic)

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
