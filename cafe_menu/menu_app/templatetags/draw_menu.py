# from django import template
# from menu_app.models import MenuItem

# register = template.Library()

# @register.simple_tag
# def draw_menu(menu_name):
#     menu_items = MenuItem.objects.filter(parent=None).prefetch_related('children')
#     return menu_items


# from django import template
# from menu_app.models import MenuItem

# register = template.Library()

# @register.simple_tag(takes_context=True)
# def draw_menu(context, menu_name):
#     current_url = context['request'].path
#     menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children').all()
    
#     def build_menu(items, parent=None):
#         menu = []
#         for item in items:
#             if item.parent == parent:
#                 is_active = current_url == item.url
#                 is_expanded = is_active or any(child.url == current_url for child in item.children.all())
#                 menu.append({
#                     'item': item,
#                     'is_active': is_active,
#                     'is_expanded': is_expanded,
#                     'children': build_menu(items, item)
#                 })
#         return menu

#     return build_menu(menu_items)
























from django import template

from menu_app.models import Item

register = template.Library()


@register.inclusion_tag('includes/nested_menu.html', takes_context=True)
def draw_menu(context, menu):

    try:
        items = Item.objects.filter(menu__title=menu)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        selected_item_id = int(context['request'].GET[menu])
        selected_item = items.get(id=selected_item_id)
        selected_item_id_list = get_selected_item_id_list(selected_item, primary_item, selected_item_id)

        for item in primary_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(items_values, item['id'], selected_item_id_list)
        result_dict = {'items': primary_item}

    except:
        result_dict = {
            'items': [
                item for item in Item.objects.filter(menu__title=menu, parent=None).values()
                ]
            }

    result_dict['menu'] = menu
    result_dict['other_querystring'] = get_querystring(context, menu)

    return result_dict


def get_querystring(context, menu):
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = ('&').join(querystring_args)
    return querystring


def get_child_items(items_values, current_item_id, selected_item_id_list):
    item_list = [item for item in items_values.filter(parent_id=current_item_id)]
    for item in item_list:
        if item['id'] in selected_item_id_list:
            item['child_items'] = get_child_items(items_values, item['id'], selected_item_id_list)
    return item_list


def get_selected_item_id_list(parent, primary_item, selected_item_id):
    selected_item_id_list = []

    while parent:
        selected_item_id_list.append(parent.id)
        parent = parent.parent
    if not selected_item_id_list:
        for item in primary_item:
            if item['id'] == selected_item_id:
                selected_item_id_list.append(selected_item_id)
    return selected_item_id_list