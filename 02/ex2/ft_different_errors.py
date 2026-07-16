def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            if i == 4:
                print("Operation copleted successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError :{e}")
    print("All error types tested successfully")


def garden_operations(operation_number: int) -> None:
    i = int(operation_number)
    match i:
        case 0:
            int('abc')
        case 1:
            10 / 0
        case 2:
            open("kotek.txt")
        case 3:
            "kotek" + 5.7


if __name__ == "__main__":
    test_error_types()
