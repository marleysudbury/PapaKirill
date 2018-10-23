# coding=utf-8
from items import *
from evidence import *
from characters import *

room_pizzeria = [{
    "name": "Papa Kirill's",

    "description": """You, Detective Kirill Sidirov, are standing in the finest pizzeria in Chicago: Papa Kirill's. Having spent most of your childhood here with your uncle running around, knocking things over and eating free pizza, you are very familiar with the ins and outs of this eatery. You start your detective work by searching the building in the hope of finding any clues that might explain your uncle's mysterious death.

Stooping down, you examine the body:

Under a stained cooking apron lies your uncle, face down. He is dead. Garbed in a blood-stained white tuxedo with a black bow tie, six stab wounds line his back. Beside the corpse is a table. On this table sits Papa Kirill’s chef’s hat. Curiously, there is still dough on the table and there is a hand mark in the middle of it, that’s a big hand! You should inspect it.

This murder seems very personal.. Who would do this and why.. Your uncle might not be the virtuous innocent man you once thought he was..

Under the table, you notice the edge of a purple piece of paper.

The evidence here is sparse, you need to look elsewhere. The Car Park and Delivery Station is west and the Alleyway is east.""",

    "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway"},

    "items": [],

    "evidence": [evidence_dough, evidence_flyer],

    "characters": [],

},
    {
    "name": "Papa Kirill's",

    "description": """You are in the restaurant, Papa Kirill's corpse is still on the floor in the kitchen. There's a bullet on the floor.""",

    "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway"},

    "items": [item_bullet],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Papa Kirill's",

    "description": """You come out of the sewers through a secret hatch. In the kitchen is a man in a police uniform checking out your uncle's cadaver.""",

    "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway"},

    "items": [],

    "people": [],

    "evidence": [],

    "characters": [person_fakecop],
    },
    {
    "name": "Papa Kirill's",

    "description": """The fake cop is standing in the kitchen. However he is not wearing his uniform anymore, he is wearing a hat, tight trousers, a jacket and a bow tie with a cigar in his mouth. He's staring at you as he cleans the barrel of his gun.""",

    "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway", "down": "Sewers"},

    "items": [],

    "people": [],

    "evidence": [],

    "characters": [person_killer],
    }]
room_parking = [{
    "name": "Car Park and Delivery Station",

    "description": """You are in the Car Park and Delivery Station. There are a few cars scattered about the lot, presumably customers. A large mark, likely left by a tyre, heads off down the concrete road. No delivery bike could make such an imprint - it was definitely a car but which one remains a mystery. I should ask Christine.

Oh, there's a bullet on the floor.

You look around but find no other clues. To the south is a bar. To the east is the restaurant.""",

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [item_bullet],

    "evidence": [evidence_tire],

    "characters": [],

    },
    {

    "name": "Car Park and Delivery Station",

    "description": """The tire mark is still on the floor. The weird guy that was at Andy's Jazz Club jumps into the Alleyway.

Nothing else to see here.""",

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [],

    "people": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Car Park and Delivery Station",

    "description": """The tire mark is still on the floor. Nothing special to notice here apart from another bullet.""",

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [item_bullet],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Car Park and Delivery Station",

    "description": """The tire mark is still on the floor. Nothing special to notice here.""",

    "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
    }
]
room_jazzclub = [{
    "name": "Andy's Jazz Club",

    "description": """You are in Andy's Jazz Club. Christine should be playing soon. The bar is in front of you and the stage is on the right. All the tables are placed around the stage.""",

    "exits": {"north": "Car Park and Delivery Station"},

    "items": [],

    "evidence": [],

    "characters": [person_witness],

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

    "description": """You are in Andy's Jazz Club. Hand in hand you walk towards the dance floor with Octavio Ricca.""",

    "exits": {"north": "Car Park and Delivery Station"},

    "items": [],

    "evidence": [],

    "characters": [person_killer],
    }
]

room_policestation = [{
    "name": "Chicago Police Department",

    "description": """You are in the CPD. There are too many people in the waiting room. It's useless to stay here any longer.""",

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Chicago Police Department",

    "description": """You are in the CPD. A lady is at the reception. 
    
    'Hello there,' she said, 'take a seat we'll take care of you soon'.

You see Bob Smith behind a window working on something on his computer. The closer you look at him the more you think that he's playing some sort of FPS because his left hand is pretty still and his right hand moves vigorously across the table.""",

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Chicago Police Department",

    "description": """You enter the CPD and the reception lady makes you sit down to wait.

Bob Smith enters the room.""",

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [person_cop],
    },
    {
    "name": "Chicago Police Department",

    "description": """You are in the CPD. The same lady is at the reception. 

'Hello there,' she said, 'take a seat we'll take care of you soon'.

You see Bob Smith behind a window working on something on his computer. The closer you look at him the more you think that he's playing some sort of FPS because his left hand is pretty still and his right hand moves vigorously across the table.""",

    "exits": {"north": "Alleyway"},

    "items": [],

    "evidence": [],

    "characters": [],
    }
]

room_sewers = [{
    "name": "Sewers",

    "description": """You found a bug in the system. You should not be here.""",

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
},
    {

    "name": "Sewers",

    "description": """You are in the Sewers. Around you is a lot of human waste which stings your nostrils.

Behind you is the ladder you used to come down. You cannot go back up as someone closed the manhole.

On your right is a poster of Kirill on a bear.

As you walk towards it you feel something under your feet. A bunch of feces covers it.

You put your hands in the sewer and find a knife""",

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [evidence_poster, evidence_knife],

    "characters": [],
    },
    {
    "name": "Sewers",

    "description": """It smells horrible down here. If you stay too long you might get a headache.

You can only go back up to Papa Kirill's""",

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
    },
    {
    "name": "Sewers",

    "description": """It smells horrible down here. If you stay too long you might get a headache.

You can only go back up to Papa Kirill's""",

    "exits": {"up": "Papa Kirill's"},

    "items": [],

    "evidence": [],

    "characters": [],
    }
]

room_alleyway = [{
    "name": "Alleyway",

    "description": """You are in the Alleyway. Do not spend too much time here or you might get snatched up by someone.""",

    "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department"},

    "items": [],

    "evidence": [],

    "characters": [],
},
    {

    "name": "Alleyway",

    "description": """You are in the Alleyway. The shady guy that was in the corner of Andy's Jazz Club is no where to be seen even though you saw him pop in the Alleyway.

Walking down the Alleyway you almost trip over a drunk person that was lying there.""",

    "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department", "down": "Sewers"},

    "items": [],

    "evidence": [evidence_drunkbody, evidence_manhole],

    "characters": [],
    },
    {

        "name": "Alleyway",

        "description": """The drunk man's body is still on the side where you left him. The manhole is slightly open.""",

        "exits": {"south": "Chicago Police Department", "west": "Papa Kirill's", "down": "Sewers"},

        "items": [],

        "evidence": [],

        "characters": [],
    },
    {

        "name": "Alleyway",

        "description": """The drunk man's body is still on the side where you left him. The manhole is slightly open.""",

        "exits": {},

        "items": [item_bullet],

        "evidence": [],

        "characters": [],
    }
]


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
        from game import room_ver
        this_room = rooms[room][room_ver]
        if this_room['name'] == name:
            for item in this_room['items']:
                if item['id'] == identity:
                    return rooms[room][room_ver]['items'].pop(index)
                index += 1
    return False
