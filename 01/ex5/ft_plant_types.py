class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self._name = name
        self._growth_rate = growth_rate

        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            self._height_cm = 0.0
        else:
            self._height_cm = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age_days = 0
        else:
            self._age_days = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height_cm, 1)}cm," +
              f"{round(self._age_days)} days old")

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
            print(f"Height updated: {round(self._height_cm, 1)} cm")

    def set_age(self, days: int) -> None:
        if days < 0.0:
            print(f"{self._name}: Error, Age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = days
            print(f"Age updated: {round(self._age_days, 1)} days")

    def get_height(self) -> float:
        return self._height_cm

    def get_age(self) -> float:
        return self._age_days

    def get_param_height(self) -> float:
        return self._growth_rate


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color):
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self._has_bloomed is False):
            print("Rose has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int, growth_rate: float,  trunk_diameter: float):
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self._name} now produces a shade of {self._height_cm} long and {self._trunk_diameter} wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 harvest_season: str, nutritional_value: float):
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutrition value: {round(self._nutritional_value, 1)}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.7

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.7


if __name__ == "__main__":
    flower1 = Flower("Rose", 15.0, 10, 0.8, "red")
    tree1 = Tree("Oak", 200.0, 365, 0.8, 5.0)
    vegetable1 = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0.0)

    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower1.show()
    print("[asking the rose to bloom]")
    flower1.bloom()
    flower1.show()

    print("=== Tree")
    tree1.show()
    tree1.produce_shade()

    print("=== Vegetable")
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        vegetable1.grow()
        vegetable1.age()

    vegetable1.show()
