
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        str = ""

        if self.props == None:
            return str

        for prop in self.props:
            str += f" {prop}=\"{self.props[prop]}\""

        return str
    

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"