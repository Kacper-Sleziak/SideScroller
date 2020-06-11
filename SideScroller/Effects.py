def Effect(character, id):
    if id == 0:
        pass
    elif id == 1:
        character.addStamina(50)
    elif id == 2:
        character.addMana(50)
    elif id == 3:
        character.addHealth(50)
    elif id == 4:
        del character
    elif id == 5:
        character.addHealth(-50)
    elif id == 6:
        character.addHealth(-100)

