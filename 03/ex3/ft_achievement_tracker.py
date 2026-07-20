import random


def gen_player_achievements() -> set[str]:
    achievements_list = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind',
        'Unstoppable',
        'Hidden Path Finder'
    ]
    howmany = random.randint(4, 9)
    chosen = random.sample(achievements_list, howmany)
    return set(chosen)


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("=== Achievement Tracker System === \n\n")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    all_achievements = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievements}")
    together = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {together}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
