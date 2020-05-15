# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items

    def move(self, direction):
        if hasattr(self.room, f"{direction}"):
            self.room = getattr(self.room, f"{direction}")
        else:
            print("\n\nYou cannot walk that way.\n\n")

    def pick_up(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.items.append(item)
            print(f"\n\nPlayer has picked up: {item}")
            print(f"View your inventory at any time by typing 'inventory'\n\n")
        else:
            print("\n\nThat item does not exist.\n\n")

    def inventory(self):
        return [item.__str__() for item in self.items]

    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            self.room.items.append(item)
            print(f"\n\nPlayer has dropped item: {item}\n\n")
        else:
            print("\n\nThat item does not exist.\n\n")

    def __str__(self):
        return f"to Player: {self.room}"
