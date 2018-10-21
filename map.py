from items import *
from evidence import *
from characters import *

room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike. Next to you is the School of Computer Science and Informatics reception. The receptionist, Matt Strangis, seems to be playing an old school text-based adventure game on his computer. There are corridors leading to the south and east. The exit is to the west. There is some dough on the side counter, hmm.""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook],

    "people": [person_barman], #added barman so i can test in reception, he will be moved later on

    "evidence": [evidence_dough]
}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning agains the door of the systems managers' room. Inside you notice Matt "MJ" John and Simon Jones. They ignore you. To the north is the reception.""",

    "exits":  {"north": "Reception"},

    "items": [],

    "evidence": []
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently stares at his huge monitor, ignoring you completely. On the desk you notice a cup of coffee and an empty pack of biscuits. The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": [],

    "evidence": []
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot. You can go south to the COMSC reception, or east to the general office.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": [],

    "evidence": []
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at 30-36 Newport Road. The cashier looks at you with hope in their eyes. If you go west you can return to the Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "people": [person_cop],

    "items": [item_pen, item_revolver],

    "evidence": []
}

rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}


def pop_room_item(identity, name):
    index = 0
    for room in rooms:
        this_room = rooms[room]
        if this_room['name'] == name:
            for item in this_room['items']:
                if item['id'] == identity:
                    return rooms[room]['items'].pop(index)
                index += 1
    return False
