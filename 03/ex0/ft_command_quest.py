import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program Name :{sys.argv[0]}")
    if (len(sys.argv) > 1):
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg} ")
    else:
        print("No argument recived")
    print(f"Sum of arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
