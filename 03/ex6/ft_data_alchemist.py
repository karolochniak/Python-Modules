import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    initial_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized = [name for name in initial_players if name.istitle()]
    print(f"New list of capitalized names only: {only_capitalized}")

    score_dict = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores = {k: v for k, v in score_dict.items() if v > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
