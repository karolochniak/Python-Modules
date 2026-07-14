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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant('Rose', 15.0, 10, 0.8)
    print("Plant created: ", end="")
    plant1.show()

    plant1.set_height(25)
    plant1.set_age(30)

    plant1.set_height(-15)
    plant1.set_age(-10)

    print("Current state: ", end="")
    plant1.show()
