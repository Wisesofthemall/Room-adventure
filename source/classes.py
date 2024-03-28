
import random


class Monster:

    def __init__(self, name):
        self._name = name
        self._image = ""
        self._difficulty = 1
        self._strikes = 3
        self._loot = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def difficulty(self):
        return self._name

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    @property
    def strikes(self):
        return self._strikes

    @strikes.setter
    def strikes(self, value):
        self._strikes = value

    @property
    def loot(self):
        return self._loot


    @loot.setter
    def loot(self, value):
        self._loot = value

    def increaseDifficulty(self):
        self._difficulty +=1

    def resetStrikes(self):
        self._strikes = 3

    def decreaseStrikes(self):
        self._strikes -=1

class SkullFace(Monster):
    def __init__(self):

        self._name = "Skull Face"
        self._target_number = random.randint(1, 10)
        self._solved = False
        self._instruction = "You must guess a number 1 - 10 in order to defeat me !!!"


    @property
    def solved(self):
        return self._solved

    @property
    def name(self):
      return self._name

    @name.setter
    def name(self, value):
      self._name = value

    @solved.setter
    def solved(self, value):
        self._solved = value

    def guess(self, number):

        if number < self._target_number:

            return "Higher"
        elif number > self._target_number:
            return "Lower"
        else:
            self._solved = True
            return "Correct"



###########################################################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, image, description, exits (e.g., south), exit locations (e.g., to the
        # south is room n), items (e.g., table), item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = set([])

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.add(item)

    def removeGrabbable(self, item):
        self._grabbables.remove(item)


    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table
    #  Exits: east south
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        s += "You can take: "
        for items in self._grabbables:
            s += items + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        return s

class MonsterRoom(Room):
    def __init__(self,  name, image, monster = None, roomImage =""):
        super().__init__(name, image)
        self._monster = monster
        self._solved = False
        self._roomImage = roomImage

    @property
    def monster(self):
        return self._monster

    @monster.setter
    def monster(self, value):
        self._monster = value

    @property
    def roomImage(self):
      return self._roomImage

    @roomImage.setter
    def roomImage(self, value):
      self.roomImage = value



class LockedRoom(Room):
    def __init__(self,  image,name, direction, key):
        super().__init__(name,image)
        self._locked = True
        self._direction = direction
        self._key = key
        self._image = "../assets/image/rooms/closeDoor.png"
        self._roomImage = "../assets/image/rooms/openDoor.png"

    @property
    def roomImage(self):
        return self._roomImage

    @roomImage.setter
    def roomImage(self, value):
        self._roomImage = value

    @property
    def openImage(self):
      return self._openImage

    @openImage.setter
    def openImage(self, value):
      self.openImage = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value