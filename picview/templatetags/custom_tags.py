from django import template

register = template.Library()

@register.tag
def escape(parser, token):
    nodelist = parser.parse(('endescape',))
    parser.delete_first_token()
    return EscapedNode(nodelist)


class EscapedNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return output.replace('"', '\\"').replace('\n', '\\n')