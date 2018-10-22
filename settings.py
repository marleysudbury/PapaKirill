menu_should_show = True


def toggle_menu():
    global menu_should_show
    menu_should_show = not menu_should_show
    return menu_should_show
