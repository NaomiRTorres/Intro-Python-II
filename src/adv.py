from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

backback = Item('backpack', 'small backpack to hold items')
lantern = Item('lantern', 'Lanter to help light your path')
sword = Item('sword', 'Long blade steel sword, could come in handy')
compass = Item('compass', 'compass to navigate your way')
treasure = Item('treasure', 'treasure chest filled with gold coins')

room['outside'].items.append(backback)
room['foyer'].items.append(lantern)
room['overlook'].items.append(sword)

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
print("***************************************************")
player_name = input("Enter character name: ")
player = Player(player_name, room['outside'])
print(f"Get ready to start your quest {player.name}!")
print("\n***************************************************")


while True:

    print(f"\n{player.room.name}, {player.room.description}")
    for item in player.room.items:
        print(f"\nItems in current room: {item.item_name}")

    print(f"\nItems in your inventory:", player.inventory)


    cmd = input("~~~> Choose an option: [n] North [s] South [e] East [w] West [q] Quit\n" ).lower()

    if len(cmd) == 1:
        if cmd in ["n", "s", "e", "w"]:
            player.travel(cmd)
        elif cmd == "q":
            print("Rest up for your next quest")
            exit()
        else:
            print("I did not understand that command.")

    if len(cmd) >= 2:
        if cmd == f'get {item.item_name}':
            player.add_items(item)
            # room.remove_item(item)
        if cmd == f'drop {item.item_name}':
            player.drop_items(item)
        if cmd =='view':
            player.view_inventory()
        else:
            print("\nEnter get item or drop item to add/remove items from your inventory")
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
