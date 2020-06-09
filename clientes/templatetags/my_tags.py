from django import template
from datetime import datetime

register = template.Library()


# Tag para retornar a hora atual, usado no rodapé do site
@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.now().strftime(format_string)


