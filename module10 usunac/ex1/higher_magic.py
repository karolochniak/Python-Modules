from collections.abc import Callable

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Returns a new function that executes both spells and returns a tuple of their results."""
    def combined_spell(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Returns a spell with multiplied power."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Casts a spell only if the condition function returns True."""
    def conditionally_cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditionally_cast

def spell_sequence(spells: list[Callable]) -> Callable:
    """Executes a list of spells sequentially and returns a list of results."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence

if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"
    
    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res = combined("Dragon", 50)
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("\nTesting power amplifier...")
    def dmg_spell(target: str, power: int) -> str:
        return str(power)
    
    amp = power_amplifier(dmg_spell, 3)
    print(f"Original: 10, Amplified: {amp('Target', 10)}")
