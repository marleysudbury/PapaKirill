from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
rounds = 5
health_points = 100
player_steps = 0
current_room = rooms["Reception"]


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
