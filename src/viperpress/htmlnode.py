from typing import Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list["HTMLNode"]] = None,
        props: Optional[dict[str, str]] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or not self.props:
            return ""

        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'

        return html

    def __repr__(self):
        val = ""
        if self.value:
            val = self.value
        elif self.children:
            for child in self.children:
                val += repr(child)
        props = self.props_to_html()

        if self.tag:
            return f"<{self.tag}{props}>{val}</{self.tag}>"

        return val
