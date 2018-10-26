import items
import map

# Player properties.
inventory = [items.item_revolver]
evidence = []
speech = []
rounds = 0
health_points = 100
player_steps = 0
current_room = map.rooms["Papa Kirill's"]


# Player methods.
def pop_inventory_item(identity):
    index = 0
    for item in inventory:
        if item['id'] == identity:
            return inventory.pop(index)
        index += 1
    return False


def item_is_in_list(key, value):
    for item in inventory:
        if item[key] == value:
            return True
    return False
