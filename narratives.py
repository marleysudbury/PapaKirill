import player
import map


def demo(room_ver):
    if room_ver == 0 and player.current_room == map.rooms["Papa Kirill's"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Papa Kirill's"]["version"] = 1
    if room_ver == 0 and player.current_room == map.rooms["Andy's Jazz Club"] and len(player.current_room["rooms"][room_ver]['characters']) == 0:
        map.rooms["Andy's Jazz Club"]["version"] = 1
    if room_ver == 1 and player.current_room == map.rooms["Andy's Jazz Club"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Alleyway"]["version"] = 1
    if room_ver == 1 and player.current_room == map.rooms["Alleyway"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Alleyway"]["version"] = 2
    if player.current_room == map.rooms["Papa Kirill's"] and len(player.evidence) == 7:
        global win_condition
        win_condition = True
