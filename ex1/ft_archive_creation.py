import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], 'r')
        kot = file.read()
        print(kot)
        file.close()
        print(f"File '{sys.argv[1]}' closed")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    except PermissionError as t:
        print(f"Error opening file '{sys.argv[1]}': {t}")
        return
    print("\nTransform data:")
    lines = kot.splitlines()
    transformed_lines = [line + "#" for line in lines]
    transformed_content = "\n".join(transformed_lines) + "\n"
    print(transformed_content, end="")
    print()
    new_filename = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            out_file = open(new_filename, 'w')
            out_file.write(transformed_content)
            out_file.close()
            print(f"Data saved in file '{new_filename}'.")
        except PermissionError as e:
            print(f"Error saving file '{new_filename}': {e}")


if __name__ == "__main__":
    main()
