from django import template

from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag("includes/nested_menu.html", takes_context=True)
def draw_menu(context, menu):
    try:
        items = MenuItem.objects.filter(menu__name=menu)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        selected_item_id = items.get(
            named_url=context["request"].path.split("/")[-2]
        ).id
        selected_item = items.get(id=selected_item_id)
        selected_item_id_list = get_selected_item_id_list(
            selected_item, primary_item, selected_item_id
        )
        for item in primary_item:
            if item["id"] in selected_item_id_list:
                item["child_items"] = get_child_items(
                    items_values, item["id"], selected_item_id_list
                )
        result_dict = {"items": primary_item}
    except MenuItem.DoesNotExist:
        result_dict = {
            "items": [
                item
                for item in MenuItem.objects.filter(
                    menu__name=menu, parent=None
                ).values()
            ]
        }
    result_dict["menu"] = menu
    return result_dict


def get_child_items(items_values, current_item_id, selected_item_id_list):
    item_list = [
        item for item in items_values.filter(
            parent_id=current_item_id
        )
    ]
    for item in item_list:
        if item["id"] in selected_item_id_list:
            item["child_items"] = get_child_items(
                items_values, item["id"], selected_item_id_list
            )
    return item_list


def get_selected_item_id_list(parent, primary_item, selected_item_id):
    selected_item_id_list = []

    while parent:
        selected_item_id_list.append(parent.id)
        parent = parent.parent
    if not selected_item_id_list:
        for item in primary_item:
            if item["id"] == selected_item_id:
                selected_item_id_list.append(selected_item_id)
    return selected_item_id_list
