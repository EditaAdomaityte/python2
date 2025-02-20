from datetime import date


class Tiger:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def available(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )

    def __str__(self):
        return f"{self.name} is a {self.species}"
