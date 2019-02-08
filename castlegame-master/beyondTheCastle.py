# Ryan, room 1

def magic_room():
    print("magic_room")
    
def bug_room():
    print("bug_room")

def ogre_room():
    print("This room has an 8 foot ogre.")
    print("The ogre does the roar")
    print("The ogre turns around")
    print("""Do you want to sneak around it or hit it in the back of the head?""")
    sword = False

    while True:
        choice = input("> ")
        if "sneak" in choice:
            print("You sneak around the ogre and find a sword near the next exits")
            print("There is a door to your left and right, which door do you go through?")
            
            if "take" in choice:
                sword = True
                print("You took the sword but you can't fight because you don't know how to wield a sword.")
                print("To learn, remember these words, \"Gladius ad Deum\"")
            door1 = input("> ")
            if "right" in door1:
                magic_room()
            elif "left" in door1:
                bug_room()
            
        elif "hit" in choice:
            print("You feel like you're Chuck Norris and punch the ogre in the back of the head.")
            print("This causes the ogre to fall on the ground and fall into a coma")
            print("You spot a sword near the next exits.")
            door2 = input("> ")
            if "right" in door2:
                magic_room()
            elif "left" in door2:
                bug_room()
        
        else:
            print("I got no idea what that means.")
            
ogre_room()