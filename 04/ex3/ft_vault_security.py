def secure_archive(file_name: str, operation: int = 0,
                   content: str = "") -> tuple[bool, str]:
    if operation == 0:
        try:
            with open(file_name, 'r') as file:
                k = file.read()
                return (True, str(k))
        except Exception as e:
            return (False, str(e))
    if operation == 1:
        try:
            with (open(file_name, 'w')) as file:
                file.write(content)
                return (True, "Content successfully writen")
        except Exception as t:
            return (False, str(t))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from from a nonexistent file: ")
    print(secure_archive("/not/existing/file", 0))
    print()
    print("using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 0))
    print()
    print("Using 'secure_archive' to read from from a regular file: ")
    print(secure_archive("kotek.txt", 0))
    print()
    print("Using 'secure_archive' to write previous content to a new file: ")
    print(secure_archive("newcat.txt", 1, "small shit"))


if __name__ == "__main__":
    main()
