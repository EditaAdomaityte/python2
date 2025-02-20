from datetime import date

class Eel:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"