from viperpress.textnode import TextNode, TextType
import viperpress.htmlnode as html


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
