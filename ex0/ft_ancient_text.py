import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], 'r')
        kot = file.read()
        print(kot)
        file.close()
        print(f"File '{sys.argv[0]}' closed")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as t:
        print(f"Error opening file '{sys.argv[1]}': {t}")


if __name__ == "__main__":
    main()
