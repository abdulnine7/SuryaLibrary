from django import template
register = template.Library()

@register.filter(name='range')
def get_range(number):
    return range(number)
