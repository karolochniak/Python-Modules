import functools
import operator
from collections.abc import Callable
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduces a list of spell powers using the specified operation."""
    if not spells:
        return 0
        
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
        
    return functools.reduce(ops[operation], spells)

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Returns spell variants with partially applied arguments."""
    return {
        "fire": functools.partial(base_enchantment, power=50, element="Fire"),
        "frost": functools.partial(base_enchantment, power=50, element="Frost"),
        "arcane": functools.partial(base_enchantment, power=50, element="Arcane")
    }

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculates the Fibonacci sequence with memoization optimization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable[[Any], str]:
    """Dispatcher system recognizing different types of cast spells."""
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return spell

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return dispatcher

if __name__ == "__main__":
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([20, 30, 50], 'add')}")
    print(f"Product: {spell_reducer([10, 40, 60], 'multiply')}")
    print(f"Max: {spell_reducer([10, 40, 20], 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f"Damage spell: {dispatch(42)}")
    print(f"Enchantment: {dispatch('fireball')}")
    print(f"Multi-cast: {dispatch([1, 2, 3])}")
    print(dispatch({'a': 1}))
