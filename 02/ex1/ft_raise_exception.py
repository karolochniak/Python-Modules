def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp > 40):
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if (temp < 0):
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    print("Input data is '25'")
    try:
        print(f"Temperature is now {input_temperature('25')}°C")
    except ValueError as t:
        print(f"Caught input_temperature error: {t}")

    print("Input data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature('abc')}°C")
    except ValueError as t:
        print(f"Caught input_temperature error: {t}")

    print("Input data is '100'")
    try:
        print(f"Temperature is now {input_temperature('100')}°C")
    except ValueError as t:
        print(f"Caught input_temperature error: {t}")

    print("Input data is '-50'")
    try:
        print(f"Temperature is now {input_temperature('-50')}°C")
    except ValueError as t:
        print(f"Caught input_temperature error: {t}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
