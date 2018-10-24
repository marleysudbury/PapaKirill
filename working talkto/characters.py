# intro is text that is presented to the player the first time they TALK to the char (not meet), but the next
# time you talk to the char the text changes slightly.


person_detective = {
    "name": "Kirill Sidirov",

    "intro": "[THIS IS KIRILL'S INTRO]",

    "dialog": {
        1: {
            1: "text1 choice one",
            2: "text1 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        2: {
            1: "text2 choice one",
            2: "text2 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        3: {
            1: "text3 do choice one",
            2: "text3 do choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        4: "FINAL REPEATED RESPONSE\n"  # Final message which gets printed again and again.
    }
}

person_barman = {
    "name": "Andy Silver",

    "intro": "[THIS IS ANDY'S INTRO]",

    "dialog": {
        1: {
            1: "text1 choice one",
            2: "text1 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        2: {
            1: "text2 choice one",
            2: "text2 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        3: {
            1: "text3 do choice one",
            2: "text3 do choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        4: "FINAL REPEATED RESPONSE\n"  # Final message which gets printed again and again.
    }
}

person_killer = {
    "name": "Octavio Ricca",

    "intro": "[THIS IS OCTAVIO'S INTRO]",

    "dialog": {
        1: {
            1: "text1 choice one",
            2: "text1 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        2: {
            1: "text2 choice one",
            2: "text2 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        3: {
            1: "text3 do choice one",
            2: "text3 do choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        4: "FINAL REPEATED RESPONSE\n"  # Final message which gets printed again and again.
    }
}

person_cop = {
    "name": "Bob Smith",

    "intro": "[THIS IS BOB'S INTRO]",

    "dialog": {
        1: {
            1: "text1 choice one",
            2: "text1 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        2: {
            1: "text2 choice one",
            2: "text2 choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        3: {
            1: "text3 do choice one",
            2: "text3 do choice two",
            3: "RESPONSE 1\n",
            4: "RESPONSE 2\n"
        },
        4: "FINAL REPEATED RESPONSE\n"  # Final message which gets printed again and again.
    }
}

characters = {
    "kirill": [person_detective, 0],
    "andy": [person_barman, 0],
    "christine": [person_witness, 0],
    "octavio": [person_killer, 0],
    "bob": [person_cop, 0]
}
