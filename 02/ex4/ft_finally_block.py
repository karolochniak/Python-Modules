class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name} [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        valid_plants = ['Tomato', 'Lettuce', 'Carrots']
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        invalid_plants = ['Tomato', 'lettuce', 'Carrots']
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
