from django import template

register=template.Library()

# @register.filter(name='get_val')
# def get_val(dict, key):
#     return dict.get(key,[])


# SAME USER SAME IMAGE
@register.filter
def avatar(name):
    if not name:
        return 1
    name_hash = sum(ord(char) for char in str(name))
    return (name_hash % 8) + 1


# GET REPLIES FROM DICTIONARY
@register.filter
def get_val(dictionary, key):
    return dictionary.get(key, [])
