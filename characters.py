
#intro is text that is presented to the player the first time they TALK to the char (not meet), but the next
#time you talk to the char the text changes slightly.


person_detective = {
    "name": "Kirill Sidirov",

    "dialog": {
        "intro": "",
        "text1": "",
        "text2": "",
        "text3": "",
        "text4": ""
    }

}

person_barman = {
    "name": "Andy Silver",

    "dialog": {

        "intro": """
        
Andy:
Hi, my names Andy Silver.
What can I get you?
                    
[need to give andy money for the pint of larger for info
on the woman that is witness]""",

        "text1": """
        
Kirill:
I'm looking for any information regarding the incident that at the
pizza place last night?
                    
Andy:
Ah, yes I heard from the woman over there that something had happened last night,
terrible stuff really but she didn't go into much detail so I couldn't tell
you more even if i wanted to.""",

        "text2": """
        
Andy:
Hi again, what can I get you?
                    
Kirill:
What was it you said again?
                    
Andy:
Ah, yes I heard from the woman over there that something had happened last night,
terrible stuff really but she didn't go into much detail so I couldn't tell
you more even if i wanted to.""",

        "text3": """
Andy:
If you talk to the woman sitting over there, you might get some more information."""

    }

}

person_witness = {
    "name": "Christine Szymankowszczyzna",

    "dialog": {
        "intro": """Christine has been living in Chicago for 15 years. You ask
                    her if she saw anything abnormal the night Papa Kirill was murdered.
                    She remembers seeing a 1953 Cadillac revealed that
                    FILL IN HERE did see something weird.
                    [refer to google doc for correct text, this is testing]""",
        "text1": "Christine is tired of you asking her how she lived in chic for 15 years",
        "text2": "",
        "text3": "",
        "text4": ""
    }

}

person_killer = {
    "name": "Octavio Ricca",

    "dialog": {
        "intro": "",
        "text1": "",
        "text2": "",
        "text3": "",
        "text4": ""
    }

}

person_cop ={
    "name": "Bob Smith",

    "dialog": {
        "intro": "",
        "text1": "",
        "text2": "",
        "text3": "",
        "text4": ""
    }

}

characters = {
    "Kirill": person_detective,
    "Andy": person_barman,
    "Christine": person_witness,
    "Octavio": person_killer,
    "Bob": person_cop,
}

print(person_barman["dialog"]["text1"])