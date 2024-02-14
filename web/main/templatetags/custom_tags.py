from django import template

register = template.Library()

@register.filter
def any_unread(messages):
    if messages is None:
        return False
    return any(not message.answer for message in messages)