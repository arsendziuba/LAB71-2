class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number

    def storage_place(self):
        if self.number < 0:
            return "out of stock"
        elif 0 <= self.number < 100:
            return "warehouse"
        else:
            return "Remote warehouse"

    def plus(self, count):
        self.number += count

    def minus(self, count):
        self.number -= count

# Creating two Building objects
white_bricks = Building("Bricks", "White", 300)
brown_planks = Building("Planks", "Brown", 20)

# Printing the initial state
print(f"{white_bricks.material} in {white_bricks.color}: {white_bricks.number} ({white_bricks.storage_place()})")
print(f"{brown_planks.material} in {brown_planks.color}: {brown_planks.number} ({brown_planks.storage_place()})")

# Adding 50 bricks and removing 3 planks
white_bricks.plus(50)
brown_planks.minus(3)

# Printing the updated state
print(f"{white_bricks.material} in {white_bricks.color}: {white_bricks.number} ({white_bricks.storage_place()})")
print(f"{brown_planks.material} in {brown_planks.color}: {brown_planks.number} ({brown_planks.storage_place()})")
