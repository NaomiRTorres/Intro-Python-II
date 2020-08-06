# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

        # directions
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

        

    def __str__(self):
        return f"{self.name}\n\n{self.description}"
    
    def get_items(self):
        return self.items   