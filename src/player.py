# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room

    def move(self, direction):
        if hasattr(self.room, f"{direction}"):
            self.room = getattr(self.room, f"{direction}")
        else:
            print("You cannot walk that way.")

    def __str__(self):
        return f"to Player: {self.room}"
