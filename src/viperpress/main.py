from viperpress.htmlnode import HTMLNode
from viperpress.textnode import TextNode, TextType


def main() -> None:
    node = TextNode("Some text", TextType.Bold)
    print(node)

    html = HTMLNode("h1", "My title!", props={"class": "title"})
    print(html)


if __name__ == "__main__":
    main()
