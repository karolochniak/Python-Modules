import functools
import time
from collections.abc import Callable

def spell_timer(func: Callable) -> Callable:
    """Measures and prints function execution time with 3 decimal places precision."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    """Validates if the power parameter in the cast spell is sufficient."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power')
            if power is None:
                # Automatically detects the power parameter from the provided int arguments
                for arg in reversed(args):
                    if isinstance(arg, int):
                        power = arg
                        break
                        
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:
    """Automatically retries a spell in case an exception is raised."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validates a mage name using a static method."""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Casts a spell instance (requires power >= 10)."""
        return f"Successfully cast {spell_name} with {power} power"

if __name__ == "__main__":
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Result: Fireball cast!"
    
    print(fireball())

    print("\nTesting retrying spell...")
    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise ValueError("Fizzle")
    
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex The Great"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
