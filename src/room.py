# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def items_list(self):
        return [item.__str__() for item in self.items]

    def __str__(self):
        return f"You have entered room: {self.name}. It is {self.description}"
