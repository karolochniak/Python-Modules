import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
              file=sys.stderr)
        return
    except PermissionError as t:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {t}",
              file=sys.stderr)
        return
    print("\nTransform data:")
    lines = kot.splitlines()
    transformed_lines = [line + "#" for line in lines]
    transformed_content = "\n".join(transformed_lines) + "\n"
    print(transformed_content, end="")
    print()
    print("Enter new file name (or empty): ", end="")
    new_filename = sys.stdin.readline()
    new_filename = new_filename.strip()
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
            print(f"[STDERR] Error saving file '{new_filename}': {e}",
                  file=sys.stderr)


if __name__ == "__main__":
    main()
