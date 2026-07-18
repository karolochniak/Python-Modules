import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    try:
        scores = [int(arg) for arg in sys.argv[1:]]
        print(f"Scores provide: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len (scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)} ")
    except ValueError:
        print("")

if __name__ == "__main__":
    main()