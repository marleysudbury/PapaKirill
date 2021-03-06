# coding=utf-8
import items
import evidence

characters = {
    "christine": {
        "name": "Christine Szymankowszczyzna",
        "speech": "That man over there arrived just before you."
    },
    "killer": {
        "name": "Octavio Ricca",
        "speech": "Ah look, there he is..."
    }
}

room_pizzeria = {
    "visited": False,
    "version": 0,
    "name": "Papa Kirill's",
    "rooms": [
        {
            "name": "Papa Kirill's",

            "description": """You, Detective Kirill Sidirov, are standing in the finest pizzeria in Chicago: Papa Kirill's. Having spent most of your childhood here with your uncle running around, knocking things over and eating free pizza, you are very familiar with the ins and outs of this eatery. You start your detective work by searching the building in the hope of finding any clues that might explain your uncle's mysterious death.

Stooping down, you examine the body:

Under a stained cooking apron lies your uncle, face down. He is dead. Garbed in a blood-stained white tuxedo with a black bow tie, six stab wounds line his back. Beside the corpse is a table. On this table sits Papa Kirill's chef's hat. Curiously, there is still DOUGH on the table and there is a hand mark in the middle of it, that's a big hand! You should inspect it.

Under the table, you notice the edge of a purple piece of paper. It looks like a FLYER.

The Car Park and Delivery Station is west and the Alleyway is east.""",

            "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway"},

            "items": [],

            "evidence": [evidence.evidence_dough, evidence.evidence_flyer],

            "characters": [],
        },
        {
            "name": "Papa Kirill's",

            "description": """You are in the restaurant, Papa Kirill's corpse is still on the floor in the kitchen. You are very familiar with the ins and outs of this eatery and it seems you've collected all the clues.""",

            "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway"},

            "items": [],

            "evidence": [],

            "characters": [],
        },
        {
            "name": "Papa Kirill's",

            "description": """You come out of the sewers through a secret hatch. In the kitchen is a man in a police uniform wearing bright blue shoes checking out your uncle's cadaver.""",

            "exits": {"west": "Car Park and Delivery Station", "east": "Alleyway"},

            "items": [items.item_bullet],

            "people": [],

            "evidence": [],

            "characters": [characters["killer"]],
        },
        {
            "name": "Papa Kirill's",

            "description": """The fake cop is standing in the kitchen. However he is not wearing his uniform anymore, he is wearing a hat, tight trousers, a jacket and a bow tie with a cigar in his mouth. On his feet are bright blue shoes. He's staring at you as he cleans the barrel of his gun.""",

            "exits": {},

            "items": [],

            "people": [],

            "evidence": [],

            "characters": [],
        }
    ]
}
room_parking = {
    "visited": False,
    "version": 0,
    "name": "Car Park and Delivery Station",
    "rooms": [
        {
            "name": "Car Park and Delivery Station",

            "description": """You are in the Car Park and Delivery Station. There are a few cars scattered about the lot, presumably customers. A large mark, likely left by a TIRE, heads off down the concrete road. No delivery bike could make such an imprint - it was definitely a car but which one remains a mystery. I should ask Christine.

You look around but find no other clues. To the south is a bar. To the east is the restaurant.""",

            "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

            "items": [],

            "evidence": [evidence.evidence_tire],

            "characters": [],
        },
        {
            "name": "Car Park and Delivery Station",

            "description": """You are in the Car Park and Delivery Station. There are a few cars scattered about the lot, presumably customers. A large mark, likely left by a tire, heads off down the concrete road. No delivery bike could make such an imprint - it was definitely a car but which one remains a mystery. I should ask Christine.

You look around but find no other clues. To the south is a bar. To the east is the restaurant.""",

            "exits": {"south": "Andy's Jazz Club", "east": "Papa Kirill's"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [],
        }
    ]
}
room_jazzclub = {
    "visited": False,
    "version": 0,
    "name": "Andy's Jazz Club",
    "rooms": [
        {
            "name": "Andy's Jazz Club",

            "description": """You are in Andy's Jazz Club. Christine should be playing soon. The bar is in front of you and the stage is on the right. All the tables are placed around the stage. It's packed. One lamp flickers in the corner, the booth lit by this lamp is occupied.""",

            "exits": {"north": "Car Park and Delivery Station"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [characters["christine"]],
        },
        {
            "name": "Andy's Jazz Club",

            "description": """You are in Andy's Jazz Club. Christine is singing on stage. The booth lit by a flickering light is vacant. You spot a pair of thick GLOVES on the floor near the booth.""",

            "exits": {"north": "Car Park and Delivery Station"},

            "items": [],

            "evidence": [evidence.evidence_gloves],

            "characters": [],
        },
        {
            "name": "Andy's Jazz Club",

            "description": """You are in Andy's Jazz Club. Christine's set has finished. She's drinking by the bar.""",

            "exits": {"north": "Car Park and Delivery Station"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [],
        }
    ]
}
room_policestation = {
    "visited": False,
    "version": 0,
    "name": "Chicago Police Department",
    "rooms": [
        {
            "name": "Chicago Police Department",

            "description": """You are in the CPD. There are too many people in the waiting room. It's useless to stay here any longer.""",

            "exits": {"north": "Alleyway"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [],
        },
        {
            "name": "Chicago Police Department",

            "description": """You are in the CPD. A lady is at the reception. A policeman with blue shoes eyes you suspiciously.""",

            "exits": {"north": "Alleyway"},

            "items": [],

            "evidence": [],

            "characters": [],
        },
        {
            "name": "Chicago Police Department",

            "description": """You are in the CPD. The counter is empty. Your evidence sits piled up on the counter, you see a care package on the floor.""",

            "exits": {"north": "Alleyway"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [],
        }
    ]
}
room_sewers = {
    "visited": False,
    "version": 0,
    "name": "Sewers",
    "rooms": [
        {
            "name": "Sewers",

            "description": """You are in the Sewers. Around you is a lot of human waste which stings your nostrils. Above you is the manhole, you can't jump that high.

On your right is a POSTER of Kirill on a bear.

As you walk towards it you feel something under your feet. A bunch of feces covers it.

You put your hands in the sewer and find a KNIFE.""",

            "exits": {"up": "Papa Kirill's"},

            "items": [],

            "evidence": [evidence.evidence_poster, evidence.evidence_knife],

            "characters": [],
        },
        {
            "name": "Sewers",

            "description": """You are in the Sewers. Around you is a lot of human waste which stings your nostrils. Behind you is the ladder you used to come down. You cannot go back up the same way.

As you walk towards it you feel something under your feet. A bunch of feces covers it.""",

            "exits": {"up": "Papa Kirill's"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [],
        }
    ]
}
room_alleyway = {
    "visited": False,
    "version": 0,
    "name": "Alleyway",
    "rooms": [
        {
            "name": "Alleyway",

            "description": """You are in the Alleyway. Do not spend too much time here or you might get snatched up by someone.""",

            "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department"},

            "items": [items.item_bullet],

            "evidence": [],

            "characters": [],
        },
        {
            "name": "Alleyway",

            "description": """You are in the Alleyway. The shady guy that was in the corner of Andy's Jazz Club is no where to be seen even though you saw him pop in the Alleyway.

Walking down the Alleyway you almost trip over a drunk person that was lying there.

Looking down, you notice the MANHOLE cover is open just a little bit. The concrete is scratched.""",

            "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department"},

            "items": [],

            "evidence": [evidence.evidence_manhole],

            "characters": [],
        },
                {
            "name": "Alleyway",

            "description": """You are in the Alleyway. The manhole cover is open. You may go down.""",

            "exits": {"west": "Papa Kirill's", "south": "Chicago Police Department", "down": "Sewers"},

            "items": [],

            "evidence": [],

            "characters": [],
        }
    ]
}

rooms = {
    "Papa Kirill's": room_pizzeria,
    "Car Park and Delivery Station": room_parking,
    "Andy's Jazz Club": room_jazzclub,
    "Chicago Police Department": room_policestation,
    "Sewers": room_sewers,
    "Alleyway": room_alleyway,
}


def pop_room_item(identity, name):
    global rooms
    for room in rooms:
        room_ver = get_room_version(rooms[room]['name'])
        this_room = rooms[room]['rooms'][room_ver]
        if this_room['name'] == name:
            index = 0
            for item in this_room['items']:
                if item['id'] == identity:
                    return rooms[room]['rooms'][room_ver]['items'].pop(index)
                index += 1
    return False


def pop_room_evidence(identity, name):
    room_ver = get_room_version(name)
    global rooms
    rooms[name]['rooms'][room_ver]['evidence'][:] = [d for d in rooms[name]['rooms'][room_ver]['evidence'] if d.get('id') != identity]


def get_room_version(name):
    global rooms
    return rooms[name]["version"]


def pop_room_character(name):
    room_ver = get_room_version(name)
    global rooms
    rooms[name]['rooms'][room_ver]['characters'] = []


def increment_room_version(name):
    global rooms
    rooms[name]["version"] += 1

