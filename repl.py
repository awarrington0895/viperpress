from viperpress.textnode import *
from viperpress.htmlnode import *
from viperpress.generator import *


node = TextNode(
    "This is text with `multiple code` blocks `within` it.  It `should` pose more of a challenge.",
    TextType.Plain,
)
new_nodes = split_nodes_delimiter([node], "`", TextType.Code)

print("REPL preloaded with values")
