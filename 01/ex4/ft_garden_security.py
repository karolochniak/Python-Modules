class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float) -> None:
        self._name = name
        self._height_cm = height
        self._age_days = age
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self._name}: {round(self._height_cm, 1)}cm, {round(self._age_days)} days old")
    def grow(self) -> None:
        self._height_cm += self._growth_rate
    def age(self) -> None:
        self._age_days += 1
    def set_height(self, param: float) -> None:
        if param < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height_cm = param
            print(f"Height updated: {round(self._height_cm, 1)}cm")
    def set_age(self, days: int) -> None:
        if days < 0.0:
            print(f"{self._name}: Error, Age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = days
            print(f"Age updated: {round(self._age_days, 1)}days")
    def get_height(self):
        return self._height_cm
    def get_age(self):
        return self._age_days

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