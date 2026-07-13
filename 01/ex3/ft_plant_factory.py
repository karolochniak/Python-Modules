class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float) -> None:
        self.name = name
        self.height_cm = height
        self.age_days = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height_cm, 1)}cm, {round(self.age_days)} days old")
    def grow(self) -> None:
        self.height_cm += self.growth_rate
    def age(self) -> None:
        self.age_days += 1

if __name__ == "__main__":
    plant1 = Plant('Rose',25.0, 30, 0.8)
    plant2 = Plant('Oak', 200.0, 365, 0.4)
    plant3 = Plant('Cactus', 5.0, 90, 0.5)
    plant4 = Plant('Sunflower', 80.0, 45, 0.1)
    plant5 = Plant('Fern', 15.0, 120, 0.9)
    garden_plants = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for i in garden_plants:
        print("Created: ",end="")
        i.show()
