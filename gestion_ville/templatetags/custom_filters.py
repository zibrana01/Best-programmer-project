from django import template

register = template.Library()
@register.filter
def attr(value, attributes):
    attrs = {}
    pairs = attributes.split(",")
    for pair in pairs:
        attr, val = pair.split(":")
        attrs[attr.strip()] = val.strip()
    value.field.widget.attrs.update(attrs)
    return value

register.filter("attr", attr)
