# this is a class in python to used for define class:

class Food:
    def __init__(self, name, category, calories):
        self.name = name
        self.category = category
        self.calories = calories

    def describe(self):
        return f"{self.name} is a {self.category} with {self.calories} calories."


apple = Food("Apple", "Fruit", 95)

print(apple.describe())
