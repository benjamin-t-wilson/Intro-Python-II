from room import Room
from player import Player
import sys
from item import Item

items = {
    "Rope": Item("Rope", "looks like it's capable of holding some weight"),
    "Unlit_Torch": Item("Unlit_Torch", "could probably be lit somehow."),
    "Grappling_Hook": Item("Grappling_Hook", "would be useful if combined with rope."),
    "Golden_Idol": Item("Golden_Idol", "looks valuable.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["Rope"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["Unlit_Torch"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["Grappling_Hook"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["Golden_Idol"]]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
is_start_of_game = True


def input_parse():
    global is_start_of_game
    if is_start_of_game:
        is_start_of_game = False
        input("Proceed at your own risk. Press enter to continue.\nType 'q' at any time to quit.\nType 'help' for a list of commands.")
    else:
        direction = input(
            "\n[n] North [e] East [s] South [w] West [q] Quit : ")
        return direction


command = input_parse()

while not command == "q":
    print(
        f"\nPlayer has entered:\n{player.room.name}, {player.room.description}\n")
    if len(player.room.items) > 0:
        print(f"This room contains items: {player.room.items_list()}")
        print(f"You can pick up items by typing 'get ITEM_NAME'\n")
    command = input_parse()
    if command == "n" or command == "e" or command == "s" or command == "w":
        player.move(f"{command}_to")
    elif "get" in command:
        player.pick_up(items[command.split(" ")[1]])
    elif "inventory" in command:
        print(f"Player currently holds: {player.inventory()}")
        print("You can drop items by typing 'drop ITEM_NAME'")
    elif "drop" in command:
        player.drop(items[command.split(" ")[1]])
    elif command == "q":
        sys.exit("Thanks for playing")
    elif command == "help":
        print("\n\nYou can say: n, e, s, w, inventory, get ITEM_NAME, drop ITEM_NAME, q\n\n")
    else:
        print("\n\nInvalid command\n\n")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
