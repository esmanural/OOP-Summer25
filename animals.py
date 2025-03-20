# Creating dictionaries for five different animals
elephant = {
    "name": "Elephant",
    "group": "Mammals",
    "number_of_legs": 4,
    "skills": ["memory", "trunk usage", "strength"]
}
parrot = {
    "name": "Parrot",
    "group": "Birds",
    "number_of_legs": 2,
    "skills": ["flying", "mimicry", "colorful feathers"]
}
dolphin = {
    "name": "Dolphin",
    "group": "Mammals",
    "number_of_legs": 0,
    "skills": ["swimming", "intelligence", "communication"]
}
turtle = {
    "name": "Turtle",
    "group": "Reptiles",
    "number_of_legs": 4,
    "skills": ["swimming", "long life", "slow movement"]
}
kangaroo = {
    "name": "Kangaroo",
    "group": "Mammals",
    "number_of_legs": 2,
    "skills": ["jumping", "pouch carrying", "strong legs"]
}
# Storing the animals in a list
animals = [elephant, parrot, dolphin, turtle, kangaroo]
# Printing each animal's information
for animal in animals:
    print(animal)
