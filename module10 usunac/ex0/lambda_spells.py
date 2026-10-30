def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sorts artifacts by power level in descending order."""
    return sorted(artifacts, key=lambda x: x.get('power', 0), reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filters mages with power equal to or greater than min_power."""
    return list(filter(lambda x: x.get('power', 0) >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    """Adds a prefix and suffix to spell names."""
    return list(map(lambda x: f"*{x}*", spells))

def mage_stats(mages: list[dict]) -> dict:
    """Returns a dictionary containing mage power statistics."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    
    max_p = max(mages, key=lambda x: x.get('power', 0))['power']
    min_p = min(mages, key=lambda x: x.get('power', 0))['power']
    avg_p = round(sum(map(lambda x: x.get('power', 0), mages)) / len(mages), 2)
    
    return {'max_power': max_p, 'min_power': min_p, 'avg_power': avg_p}

if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) comes before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal shield"]
    for spell in spell_transformer(spells):
        print(spell)
