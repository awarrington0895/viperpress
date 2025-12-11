from viperpress.textnode import TextNode, TextType


def main() -> None:
    node = TextNode("Some text", TextType.Bold)
    print(node)


if __name__ == "__main__":
    main()
