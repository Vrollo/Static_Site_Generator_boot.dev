class HTMLNode():
    def __init__(self, tag=None, value=None, children: list["HTMLNode"] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        prop_str = ""
        # might need to catch {}
        if self.props is None:
            return ""
        for key, value in self.props.items():
            prop_str += f" {key}=\"{value}\""
        return prop_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag == "" or self.tag is None:
            return self.value
        elif self.tag == "img":
            # the img tag does not have a closing tag like <a></a> or <b></b> it's just <img ......>
            # The TextNode does not have props, so can't handle additional props yet for images
            return f'<{self.tag}{self.props_to_html()}{self.value}>'
        else:   
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children: list["HTMLNode"], props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == "" or self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")

        children_html = ""

        for child in self.children:
            if child is None:
                return
            else:
                children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"