def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')} °C")
    print("Input data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature('abc')} °C")
    except ValueError as t:
        print(f"Caught input_temperature error: {t}")
    print("I will survive ;)")


if __name__ == "__main__":
    test_temperature()
