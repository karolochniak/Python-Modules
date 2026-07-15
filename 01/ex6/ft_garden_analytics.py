class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._howmanygrow = 0
            self._howmanyage = 0
            self._howshow = 0

        def display(self) -> None:
            print(f"Stats: {self._howmanygrow} grow, {self._howmanyage} age, \
{self._howshow} show")

        def increment_grow(self) -> None:
            self._howmanygrow += 1

        def increment_age(self) -> None:
            self._howmanyage += 1

        def increment_show(self) -> None:
            self._howshow += 1

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._stats = self._Stats()

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
        self._stats.increment_show()

    def grow(self) -> None:
        self._height_cm += self._growth_rate
        self._stats.increment_grow()

    def age(self) -> None:
        self._age_days += 1
        self._stats.increment_age()

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

    @classmethod
    def anonim(cls) -> 'Plant':
        return cls("Unknown Plant", 0, 0, 0)

    @staticmethod
    def check_age(age_to_check: int) -> bool:
        if (age_to_check > 365):
            return True
        else:
            return False


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color: str):
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


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):

    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._howmanyshade = 0

        def display(self) -> None:
            super().display()
            print(f"{self._howmanyshade} shade")

        def increment_shade(self) -> None:
            self._howmanyshade += 1

    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 trunk_diameter: float):
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._stats = self._TreeStats()

    def produce_shade(self):
        print(
            f"Tree {self._name} now produces a shade of {self._height_cm} long\
and {self._trunk_diameter} wide.")
        self._stats.increment_shade()

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


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    print("=== Flower")
    flower1 = Flower("Rose", 15.0, 10, 0.8, "red")
    flower1.show()
    display_plant_stats(flower1)
    print("[asking the rose to grow and bloom]")
    flower1.grow()
    flower1.bloom()
    flower1.show()
    display_plant_stats(flower1)

    print("=== Tree")
    tree1 = Tree("Oak", 200.0, 365, 0.4, 5.0)
    display_plant_stats(tree1)
    tree1.produce_shade()
    display_plant_stats(tree1)

    print("=== Seed")
    seed1 = Seed("Sunflower", 80.0, 45, 1.5, "yellow")
    seed1.show()

    print("[make sunflower grow, age and bloom]")
    for _ in range(20):
        seed1.grow()
        seed1.age()
    seed1.bloom()
    seed1.show()

    display_plant_stats(seed1)
    print("=== Anonymous")
    anon_plant = Plant.anonim()
    anon_plant.show()
    display_plant_stats(anon_plant)
