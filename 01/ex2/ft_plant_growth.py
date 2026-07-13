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
    plant = Plant('Rose',25.0, 30, 0.8)
    height = plant.height_cm
    print("=== Garden Plant Growth ===")
    plant.show()
    for i in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {i} ===")
        plant.show()
    print("Growth this week: ", round(plant.height_cm - height, 1) , "cm")