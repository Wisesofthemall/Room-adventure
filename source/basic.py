###########################################################################################
# Name: ###########################
# Description: A basic GUI Room Adventure game to show its mechanics and gameplay.
###########################################################################################

###########################################################################################
# import libraries
import random
from tkinter import *
from functools import partial
from classes import SkullFace, Room, MonsterRoom, LockedRoom, Kong, Riddler, Teddy, ExitRoom

# Now you can use the SkullFace class in your "basic.py" file

###########################################################################################
# constants
VERBS = ["go", "look", "take", "use"]  # the supported vocabulary verbs
QUIT_COMMANDS = ["exit", "quit", "bye"]  # the supported quit commands




###########################################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)


    # creates the rooms
    def createRooms(self):
        # a list of rooms will store all of the rooms
        # r1 through r4 are the four rooms in the "mansion"
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        Game.rooms = []

        # first, create the room instances so that they can be referenced below
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = MonsterRoom("Room 3", "../assets/image/monsters/skullface.png", SkullFace(), "../assets/image/rooms/skullroom.png")
        r4 = Room("Room 4")
        r5 = Room("Room 5")
        r6 = Room("Room 6")
        r7 = LockedRoom("Room 7","../assets/image/rooms/closeDoor.png" , "east", "golden_key")
        r8 = Room("Room 8")
        r9 = Room("Room 9")
        r10 = Room("Room 10")
        r11 = MonsterRoom("Room 11","../assets/image/monsters/kong.png", Kong(), "../assets/image/rooms/skullroom.png")
        r12 = Room("Room 12")
        r13 = Room("Room 13")
        r14 = MonsterRoom("Room 14","../assets/image/monsters/riddler.png",Riddler(), "../assets/image/rooms/skullroom.png")
        r15 = LockedRoom("Room 15","../assets/image/rooms/closeDoor.png" , "west", "kong_hair")
        r16 = Room("Room 16")
        r17 = MonsterRoom("Room 17","../assets/image/monsters/riddler.png",Riddler(), "../assets/image/rooms/skullroom.png")
        r18 = Room("Room 18")
        r19 = Room("Room 19")
        r21 = Room("Room 21")
        r20 = MonsterRoom("Room 20","../assets/image/monsters/kong.png", Kong(), "../assets/image/rooms/skullroom.png")
        r26 = MonsterRoom("Room 17","../assets/image/monsters/teddy.png",Teddy(), "../assets/image/rooms/skullroom.png")
        r22 = ExitRoom("Room 25","../assets/image/rooms/exit.png" )
        r25 = ExitRoom("Room 25","../assets/image/rooms/exit.png" )

        r23 =Room("Room 23")
        r24 = Room("Room 24")
        # room 1
        r1.description = "You look around the room."
        r1.addExit("east", r2)
        r1.addExit("north", r4)

        r1.addItem("chair", "It is made of wicker. No one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden_key rests on it.")
        r1.addGrabbable('key')


        # room 2
        r2.description = "This room smells funny."
        r2.addExit("west", r1)
        r2.addExit("east", r3)
        r2.addItem("rug", "It appears to be Persian. It also needs to be\nvacuumed.")
        r2.addItem("fireplace", "It is full of ashes and smells dank.")
        r2.addGrabbable('phone')
        r2.addGrabbable('map')


        # set room 1 as the current room at the beginning of the game

        # room 3 (Monster room)
        r3.description="Monster!"
        r3.addGrabbable("golden_key")
        r3.addExit("west", r2)
        r3.addExit("east", r5)


        #room 4 (Map room)
        r4.description=""
        r4.addGrabbable('phone')
        r4.addGrabbable('map')
        r4.addExit("south", r1)

        # room 5
        r5.description=""
        r5.addGrabbable('phone')
        r5.addGrabbable('map')
        r5.addExit("west", r3)
        r5.addExit("south", r6)

        # room 6
        r6.description=""
        r6.addGrabbable('phone')
        r6.addGrabbable('map')
        r6.addExit("north", r5)
        r6.addExit("east", r7) #! change to locked room

        # room 7 (Locked Room)
        r7.description=""
        r7.addExit("west", r6)
        r7.addExit("east", r8) #! change to locked room

        # Room 8
        r8.addExit("west", r7)
        r8.addExit("east", r9)

        # Room 9
        r9.addExit("west", r8)
        r9.addExit("south", r10)

        # room 10
        r10.addExit("north", r9)
        r10.addExit("south",r11)

        # Room 11 (Monster Room)
        r11.addExit("north", r10)
        r11.addExit("south", r12)
        r11.addGrabbable("kong_hair")

        # Room 12
        r12.addExit("north", r11)
        r12.addExit("south",r13)

        # Room 13
        r13.addExit("north", r12)
        r13.addExit("west", r15)
        r13.addExit("east", r14)

        # Room 14 (Monster Room)
        r14.addExit("west", r13)
        r14.addGrabbable("golden_sword")

        # Room 15 Locked Door
        r15.addExit("east", r13)
        r15.addExit("west", r16)

        # Room 16
        r16.addExit("north", r17)
        r16.addExit("east",r15)
        r16.addExit("south", r26)

        # Room 26
        r26.addExit("west", r23)
        r26.addExit("north", r16)

        #Room 17
        r17.addExit("south", r16)
        r17.addExit("west", r18)


        # Room 18
        r18.addExit("east", r17)
        r18.addExit("west", r19)


        # Room 19
        r19.addExit("west", r20)
        r19.addExit("east",r18)

        # Room 20 (Moonster Room)
        r20.addExit("west", r21)
        r20.addExit("east",r19)


        # Room 21
        r21.addExit("east", r20)
        r21.addExit("west", r22)


        # Room 25 (Exit room)
        r25.addExit("east", r24)

        # Room 22 (Exit room)
        r22.addExit("east", r21)
        # Room 23
        r23.addExit("west", r24)
        r23.addExit("east", r26)

        # Room 24
        r24.addExit("west", r25)
        r24.addExit("east", r23)

        Game.rooms.append(r1)
        Game.rooms.append(r2)
        Game.rooms.append(r3)
        Game.rooms.append(r4)
        Game.rooms.append(r5)
        Game.rooms.append(r6)
        Game.rooms.append(r7)
        Game.rooms.append(r8)
        Game.rooms.append(r9)
        Game.rooms.append(r10)
        Game.rooms.append(r11)
        Game.rooms.append(r12)
        Game.rooms.append(r13)
        Game.rooms.append(r14)
        Game.rooms.append(r15)
        Game.rooms.append(r16)
        Game.rooms.append(r17)
        Game.rooms.append(r18)
        Game.rooms.append(r19)
        Game.rooms.append(r20)
        Game.rooms.append(r21)
        Game.rooms.append(r22)
        Game.rooms.append(r23)
        Game.rooms.append(r24)
        Game.rooms.append(r25)
        Game.rooms.append(r26)

        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = set([])

        # sets up the GUI

    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process() in the class
        # bind the tab key to the function complete() in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="black")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=X)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2, height=HEIGHT // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=TOP, fill=Y)
        text_frame.pack_propagate(False)
        # Creating a canvas for the bottom half to easily navigate between roomsclear
        # Add north and south arrows as well in the code.
        # Feel free to use your own directional images.
        # North and South arrows are also provided to you as well.
        #Adding an arrow pointing to the east.
        canvas = Frame(self, width=WIDTH // 2, height=HEIGHT // 2)

        Game.northimage = PhotoImage(file="../assets/image/directions/north.png")
        Game.north = Button(canvas, image=Game.northimage, command=partial(self.runCommand, "go north"))
        Game.north.pack(side=TOP)

        Game.southimage = PhotoImage(file="../assets/image/directions/south.png")
        Game.south = Button(canvas, image=Game.southimage, command=partial(self.runCommand, "go south"))
        Game.south.pack(side=BOTTOM)

        Game.eastimage = PhotoImage(file="../assets/image/directions/east.png")
        Game.east = Button(canvas, image=Game.eastimage, command=partial(self.runCommand, "go east"))
        Game.east.pack(side=RIGHT)
        #Adding an arrow pointing to the west.
        Game.westimage = PhotoImage(file="../assets/image/directions/west.png")
        Game.west = Button(canvas, image=Game.westimage, command=partial(self.runCommand, "go west"))
        Game.west.pack(side=LEFT)

        canvas.pack(side=TOP, fill=Y)
        canvas.pack_propagate(False)

    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)

        if (isinstance(Game.currentRoom, MonsterRoom) and Game.currentRoom._monster._solved == False ):
            Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            Game.text.insert(END, "You have enter a BOSS FIGHT PREPPARE \n")
            Game.text.insert(END, "You CANNOT leave this room until the BOSS is defeated \n")
            Game.text.insert(END, Game.currentRoom._monster._instruction)
            Game.text.config(state=DISABLED)

        if (isinstance(Game.currentRoom, LockedRoom) and Game.currentRoom._locked == True ):
            Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            Game.text.insert(END, "Dang this room is locked \n")
            Game.text.insert(END, f"this door requires a {Game.currentRoom._key} to open the door \n")

        if (isinstance(Game.currentRoom, ExitRoom) ):
            Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            Game.text.insert(END, "You have EXIT THE MAZE congratulationscongratulations 🎉 \n")
            Game.text.insert(END, "Quit the game to restart \n")


        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now\nis quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, list(Game.inventory)))


        # support for tab completion
        # add the words to support
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + list(Game.inventory) + Game.currentRoom.exits + Game.currentRoom.items + list(Game.currentRoom.grabbables)
        Game.text.config(state=DISABLED)
    # play the game
    def play(self):
        # create the room instances
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus("WELCOME TO ROOM ADVENTURE!")

    # processes the player's input
    def process(self, event, action=""):
        self.runCommand()
        Game.player_input.delete(0, END)

    def runCommand(self, action=""):
        if not action.startswith("go"):
            # grab the player's input from the input at the bottom of the GUI
            action = Game.player_input.get()
            # set the user's input to lowercase to make it easier to compare the verb and noun to known values
            action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)

        if (isinstance(Game.currentRoom, MonsterRoom) and Game.currentRoom._monster._solved == False):
            Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            Game.text.insert(END, "You have enter a BOSS FIGHT PREPPARE \n")
            Game.text.insert(END, "You CANNOT leave this room until the BOSS is defeated \n")
            Game.text.insert(END, Game.currentRoom._monster._instruction + "\n")
            Game.text.insert(END, action + "\n")
            if action.isdigit():
                Game.text.insert(END, Game.currentRoom._monster.guess(int(action)))
            else:
                Game.text.insert(END, Game.currentRoom._monster.guess(action))

            if Game.currentRoom._monster._strikes == 0:
                Game.currentRoom = None
                self.setStatus(f"YOU DIED ")
            if(Game.currentRoom._monster._solved == True):
                Game.currentRoom._description = ""

                Game.currentRoom.image = Game.currentRoom.roomImage
                self.setStatus(f"YOU DEFEATED {Game.currentRoom._monster.name}, GRAB THE LOOT")

            self.setRoomImage()
            return
        if (isinstance(Game.currentRoom, LockedRoom) and Game.currentRoom._locked == True):
            words = action.split()

            # the game only understands two word inputs
            if (len(words) == 2):
                # isolate the verb and noun
                verb = words[0].strip()
                noun = words[1].strip()

                # we need a valid verb
                if (verb in VERBS):
                    # the verb is: go
                    if (verb == "go"):
                        # set a default response
                        response = "You can't go in that direction."

                        # check if the noun is a valid exit
                        if (noun in Game.currentRoom.exits and noun != Game.currentRoom._direction):
                            # get its index
                            i = Game.currentRoom.exits.index(noun)
                            # change the current room to the one that is associated with the specified exit
                            Game.currentRoom = Game.currentRoom.exitLocations[i]
                            # set the response (success)
                            response = "You walk {} and enter another room.".format(noun)
                    # the verb is: use

                    elif (verb == "use"):
                        # set a default response
                        response = "You cant use  that item."

                        if( noun in Game.inventory and noun == Game.currentRoom._key):
                            Game.inventory.remove(noun)
                            Game.currentRoom._locked = False
                            Game.currentRoom.direction = ""
                            Game.currentRoom.image = Game.currentRoom._roomImage
                            response ="YES it WORKS"

                    self.setStatus(response)
                    self.setRoomImage()
            return



        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()

            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # set a default response
                    response = "You can't go in that direction."

                    # check if the noun is a valid exit
                    if (noun in Game.currentRoom.exits):
                        # get its index
                        i = Game.currentRoom.exits.index(noun)
                        # change the current room to the one that is associated with the specified exit
                        Game.currentRoom = Game.currentRoom.exitLocations[i]
                        # set the response (success)
                        response = "You walk {} and enter another room.".format(noun)
                # the verb is: look
                elif (verb == "look"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid item
                    if (noun in Game.currentRoom.items):
                        # get its index
                        i = Game.currentRoom.items.index(noun)
                        # set the response to the item's description
                        response = Game.currentRoom.itemDescriptions[i]
                # the verb is: take
                elif (verb == "take"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid grabbable and is also not already in inventory
                    if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                        # get its index

                        # add the grabbable item to the player's inventory

                        Game.inventory.add(noun)
                        # set the response (success)
                        Game.currentRoom.removeGrabbable(noun)
                        response = "You take {}.".format(noun)

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()

    # implements tab completion in the Entry widget
    def complete(self, event):
        # get user input and the last word of input
        words = Game.player_input.get().split()
        # continue only if there are words in the user's input
        if (len(words)):
            last_word = words[-1]
            # check if the last word of input is part of a valid verb/noun
            results = [x for x in Game.words if x.startswith(last_word)]

            # initially, there is no matching verb/noun
            match = None

            # is there only a single valid verb/noun?
            if (len(results) == 1):
                # the result is a match
                match = results[0]
            # are there multiple valid verbs/nouns?
            elif (len(results) > 1):
                # find the longest starting substring of all verbs/nouns
                for i in range(1, len(min(results, key=len)) + 1):
                    # get the current substring
                    match = results[0][:i]
                    # find all matches
                    matches = [x for x in results if x.startswith(match)]
                    # if there are less matches than verbs/nouns
                    if (len(matches) != len(results)):
                        # go back to the previous substring
                        match = match[:-1]
                        # stop checking
                        break
            # if a match exists, replace the user's input
            if (match):
                # clear user input
                Game.player_input.delete(0, END)
                # add all but the last (matched) verb/noun
                for word in words[:-1]:
                    Game.player_input.insert(END, "{} ".format(word))
                # add the match
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

        # prevents the tab key from highlighting the text in the Entry widget
        return "break"


###########################################################################################
# START THE GAME!!!
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
