# coding=utf-8
from items import *
from evidence import *
from characters import *

room_pizzeria = [{
    "name": "Papa Kirill's",

    "description": """ 
    You, Detective Kirill Sidirov, are standing in the finest
    pizzeria in Chicago: Papa Kirill's. You are very familiar with the
    ins and outs of this eatery because you have spent most of your
    childhood in it with your uncle, running around, knocking things over, 
    eating free pizza. You start your detective work by searching the
    building in the hope of finding any clues that might explain your
    uncle's mysterious death.

    Firstly, you examine the body:

    Under a cooking apron, your uncle is wearing a blood-stained white
    tuxedo with a black bow tIe. Six stab wounds are on his back. 
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

    "exits": {"west": "Parking", "east": "Alleyway"},

    "items": [item_flyer],

    "evidence": [evidence_dough],

    "characters": [],

},
    {
    "name": "Papa Kirill's",

    "description": """
    You are in the restaurant, Papa Kirill's 
    corpse is still on the floor in the kitchen.
    
    There's a bullet on the floor.
    """,

    "exits": {"west": "Parking", "east": "Alleyway"},

    "items": [item_bullet],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Papa Kirill's",

    "description": """
    You come out of the sewers through a secret hatch.
    In the kitchen is a man in a police uniform checking
    out your uncle's cadaver.""",

    "exits": {"west": "Parking", "east": "Alleyway"},

    "items": [item_round],

    "people": [],

    "evidence": [],

    "characters": [character_fakecop],
    },
    {
    "name": "Papa Kirill's",

    "description": """The fake cop is standing in the kitchen. However
    he is not wearing his uniform anymore, he is wearing a hat, tight
    trousers, a jacket and a bow tie with a cigar in his mouth. He's 
    staring at you as he cleans the barrel of his gun.
    """,

    "exits": {"west": "Parking", "east": "Alleyway", "down": "Sewers"},

    "items": [item_round],

    "people": [],

    "evidence": [],

    "characters": [character_killer],
    }]
room_parking = [{
    "name": "Car Park and Delivery Station",

    "description": """
    You are in the Car Park and Delivery Station. Here is where customers 
    would park their cars to eat in the restaurant. This is also
    where delivery bikes would leave to bring food directly to the
    customers' houses. You notice a big tire mark left on the concrete
    road. No delivery bike could make such an imprint. You can tell it came
    from a car but which one remains a mystery. I should ask Christine.
    
    Oh, there's a bullet on the floor.
    
    You look around but find no other clues. To the south is a bar. To the
    east is the restaurant.
""",

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [item_bullet],

    "evidence": [evidence_tire],

    "characters": [],

    },
    {

    "name": "Car Park and Delivery Station",

    "description": """
    The tire mark is still on the floor.
    The weird guy that was at Andy's Jazz Club
    jumps into the Alleyway.
    
    Nothing else to see here.""",

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [item_round],

    "people": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Car Park and Delivery Station",

    "description": """
    The tire mark is still on the floor.
    Nothing special to notice here apart from another bullet.
    """,

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [item_bullet],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Car Park and Delivery Station",

    "description": """
    The tire mark is still on the floor.
    Nothing special to notice here.
    """,

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
    }
]
room_jazzclub = [{
    "name": "Andy's Jazz Club",

    "description": """
    You are in Andy's Jazz Club.
    Christine should be playing soon. The bar is in front
    of you and the stage is on the right. All the tables
    are placed around the stage.
    
    There's a bullet under on the floor""",

    "exits": {"north": "Car Park and Delivery Station"},

    "items": [item_bullet],

    "evidence": [],

    "characters": [character_witness],

},
    {

    "name": "Andy's Jazz Club",

    "description": """The Jazz Club is closed.
    
    Oh, another bullet is on the floor.""",

    "exits": {"north": "Car Park and Delivery Station"},

    "items": [item_bullet],

    "evidence": [],

    "characters": [],
    },
    {

    "name": "Andy's Jazz Club",

    "description": """The Jazz Club is closed""",

    "exits": {"north": "Car Park and Delivery Station"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {

    "name": "Andy's Jazz Club",

    "description": """
    You are in Andy's Jazz Club. Hand in hand you walk
    towards the dance floor with Octavio Ricca.""",

    "exits": {"north": "Car Park and Delivery Station"},

    "items": [],

    "evidence": [],

    "characters": [character_killer],
    }
]

room_policestation = [{
    "name": "Chicago Police Department",

    "description": """
    You are in the CPD. There are too many people in the 
    waiting room. It's useless to stay here any longer.
    """,

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Chicago Police Department",

    "description": """
    You are in the CPD. A lady is at the reception. 
    
    'Hello there,' she said, 'take a seat we'll take
    care of you soon'. 
    
    You see Bob Smith behind a window working on something
    on his computer. The closer you look at him the more you 
    think that he's playing some sort of FPS because his 
    left hand is pretty still and his right hand moves 
    vigorously across the table.
    """,

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Chicago Police Department",

    "description": """
    You enter the CPD and the reception lady makes
    you sit down to wait.
    
    Bob Smith enters the room.
    """,

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [character_cop],
    },
    {
    "name": "Chicago Police Department",

    "description": """
    You are in the CPD. The same lady is at the reception. 
    
    'Hello there,' she said, 'take a seat we'll take
    care of you soon'. 
    
    You see Bob Smith behind a window working on something
    on his computer. The closer you look at him the more you 
    think that he's playing some sort of FPS because his 
    left hand is pretty still and his right hand moves 
    vigorously across the table. 
    """,

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [],
    }
]

room_sewers = [{
    "name": "Sewers",

    "description": """
    You found a bug in the system.
    You should not be here.""",

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
},
    {

    "name": "Sewers",

    "description": """
    You are in the Sewers. Around you is a lot
    of human waste which stings your nostrils.
    
    Behind you is the ladder you used to come down.
    You cannot go back up as someone closed the hatch
    back up.
    
    On your right is a poster of Kirill on a bear.
    
    As you walk towards it you feel something under your
    feet. A bunch of feces covers it.""",

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [evidence_poster, evidence_knife],

    "characters": [],
    },
    {
    "name": "Sewers",

    "description": """
    It smells horrible down here. If you stay too long
    you might get a headache.
    
    You can only go back up to Papa Kirill's
    """,

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Sewers",

    "description": """
    It smells horrible down here. If you stay too long
    you might get a headache.
    
    You can only go back up to Papa Kirill's
    """,

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
    }
]

room_alleyway = [{
    "name": "Alleyway",

    "description": """
    You are in the Alleyway. Do not spend too much time here
    or you might get snatched up by someone.
    .""",

    "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department"},

    "items": [],

    "evidence": [],

    "characters": [],
},
    {

    "name": "Alleyway",

    "description": """
    You are in the Alleyway. The shady guy that was in the corner 
    of Andy's Jazz Club is no where to be seen even though you saw
    him pop in the Alleyway.
    
    Walking down the Alleyway you almost trip over a drunk person 
    that was lying there.""",

    "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department", "down": "Sewers"},

    "items": [],

    "evidence": [evidence_drunkbody, evidence_manhole],

    "characters": [],
    },
    {

        "name": "Alleyway",

        "description": """
        The drunk man's body is still on the side where you 
        left him. The manhole is slightly open.""",

        "exits": {"south": "Chicago Police Department", "west": "Papa Kirill's", "down": "Sewers"},

        "items": [],

        "evidence": [],

        "characters": [],
    },
    {

        "name": "Alleyway",

        "description": """
        The drunk man's body is still on the side where you 
        left him. The manhole is slightly open.
        """,

        "exits": {},

        "items": [item_bullet],

        "evidence": [],

        "characters": [],
    }
]

    "items": [item_biscuits, item_handbook, item_round],

rooms = {
    "Papa Kirill's": room_pizzeria,
    "Car Park and Delivery Station": room_parking,
    "Andy's Jazz Club": room_jazzclub,
    "Chicago Police Department": room_policestation,
    "Sewers": room_sewers,
    "Alleyway": room_alleyway,
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
