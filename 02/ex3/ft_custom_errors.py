class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting! \n")


def check_water() -> None:
    raise WaterError("Not enough water in the tank! \n")


def test_garden_error() -> None:
    print("=== Custom Garden Errors Demo === \n")

    try:
        print("Testing PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("Testing WaterError...")
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    try:
        print("Testing GardenError...")
        check_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        print("Testing GardenError...")
        check_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    test_garden_error()


if __name__ == "__main__":
    main()
