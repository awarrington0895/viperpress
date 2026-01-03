from viperpress.textnode import TextNode, TextType
import viperpress.htmlnode as html


class MarkdownSyntaxError(Exception):
    def __init__(self, node: TextNode):
        self.node = node
        super().__init__(f"Invalid markdown syntax: {node}")


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.Plain:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise MarkdownSyntaxError(node)

        split = node.text.split(delimiter)

        for i, part in enumerate(split):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.Plain))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.Plain:
            return html.LeafNode(tag=None, value=text_node.text)
        case TextType.Bold:
            return html.LeafNode(tag="b", value=text_node.text)
        case TextType.Italic:
            return html.LeafNode(tag="i", value=text_node.text)
        case TextType.Code:
            return html.LeafNode(tag="code", value=text_node.text)
        case TextType.Link:
            return html.LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url or ""}
            )
        case TextType.Image:
            return html.LeafNode(
                tag="img",
                value="",
                props={"src": text_node.url or "", "alt": text_node.text},
            )
        case _:
            raise ValueError(f"Invalid text node type: {text_node.text_type}")
