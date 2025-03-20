class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills
    def display_info(self):
        print(f"{self.name} ({self.group})")
        print(f"Legs: {self.number_of_legs}")
        print(f"Skills: {', '.join(self.skills)}")
        print()
# Create animal objects from Task 1
if __name__ == "__main__":
    animals = [
        Animal("Cat", "mammals", 4, ["climbing", "night vision"]),
        Animal("Eagle", "birds", 2, ["flying", "keen eyesight"]),
        Animal("Frog", "amphibians", 4, ["jumping", "swimming"]),
        Animal("Octopus", "cephalopods", 0, ["problem solving", "color changing"]),
        Animal("Crocodile", "reptiles", 4, ["ambush hunting", "powerful bite"])
    ]
    for animal in animals:
        animal.display_info()
