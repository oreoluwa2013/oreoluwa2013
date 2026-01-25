# Base class
class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print("Hello! I am a robot.")
        print(f"My name is {self.name}.")
        print(f"My model number is {self.model}.")


# Derived class (Inheritance)
class SmartRobot(Robot):
    def __init__(self, name, model, ability):
        super().__init__(name, model)
        self.ability = ability

    def show_ability(self):
        print(f"My special ability is: {self.ability}.")


# Creating an object
robot1 = SmartRobot("AIVA", "X-2026", "Artificial Intelligence Assistance")

# Calling methods
robot1.introduce()
robot1.show_ability()
