from items import *
from evidence import *
from characters import *

room_pizzeria = [{
    "name": "Papa Kirill's",

    "description": """You, Detective Kirill Sidirov, are standing in the finest
    pizzeria in Chicago: Papa Kirill's. You are very familiar with the
    ins and outs of this eatery because you have spent most of your
    childhood in it with your uncle, running around, knocking things over, 
    eating free pizza. You start your detective work by searching the
    building in the hope of finding any clues that might explain your
    uncle's mysterious death. 

    Firstly, you examine the body:

    Under a cooking apron, your uncle is wearing a blood-stained white
    tuxedo with a black bow tie. Six stab wounds are on his back. 
    Beside the corpse is a table. On this table sits Papa Kirill’s chef’s hat.
    Curiously, there is still dough on the table and there is a hand
    mark in the middle of it, that’s a big hand!
    You should take a picture of any evidence.

    After examining your uncle's corps you get a sense that this murder
    was very personal. Your uncle might not be the virtuous innocent
    man you thought he was. 

    Under the table, you notice the edge of a purple piece of paper.

    The evidence left in the restaurant was very minor, you need to look
    elsewhere. The Car Park and Delivery Station is to the west and the 
    Alleyway is to the east. You might need to check them both out to really
    get a sense of what went wrong the night of the 21rst of July 1956.
""",

    "exits": {"west": "Parking", "east": "Alleyway", "down": "Sewers"},

    "items": [item_flyer],

    "evidence": [evidence_dough],

    "characters": [],

},
    {
    "name": "Papa Kirill's",

    "description": """""",

    "exits": {"west": "Parking", "east": "Alleyway", "down": "Sewers"},

    "items": [],

    "evidence": [],

    "characters": [character_fakecop],
    }
]
room_parking = [{
    "name": "Car Park and Delivery Station",

    "description": """You are in the Car Park and Delivery Station. Here is where
    customers would park their cars to eat in the restaurant. This is also
    where delivery bikes would leave to bring food directly to the
    customers' houses. You notice a big tire mark left on the concrete
    road. No delivery bike could make such an imprint. You can tell it came
    from a car but which one remains a mystery. Hmm, perhaps we could ask
    if any locals saw a car speeding up on the main road leading up to
    the pizzeria.
    
    You look around but find no other clues. To the south is a bar. To the
    east is the restaurant.""",

    "exits": {"west": "Parking", "east": "Alleyway", "down": "Sewers"},

    "items": [item_flyer],

    "evidence": [evidence_dough],

    "characters": [],

},
    {
    
    "name": "Car Park and Delivery Station",
    
    "description": """""",

    "exits": {"west": "Parking", "east": "Alleyway", "down": "Sewers"},

    "items": [],

    "evidence": [],

    "characters": [character_fakecop],
    }
]


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
