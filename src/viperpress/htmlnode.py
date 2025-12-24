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

        # return textwrap.dedent(f"""
        #     HTMLNode(
        #         tag={self.tag},
        #         value={self.value},
        #         props={self.props},
        #         children={self.children}
        #     )
        # """)


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: Optional[dict[str, str]] = None
    ):
        super().__init__(tag=tag or None, value=value, children=None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNodes must have a value")

        if not self.tag:
            return self.value

        props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: Optional[dict[str, str]] = None
    ):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNodes must have a tag")

        if not self.children:
            raise ValueError("ParentNodes must have at least one child")

        result = ""

        for child in self.children:
            result += child.to_html()

        props = self.props_to_html()

        return f"<{self.tag}{props}>{result}</{self.tag}>"
