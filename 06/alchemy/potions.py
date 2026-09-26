from elements import create_water, create_fire
from .elements import create_air, create_earth


def healing_potion() -> str:
    return f"Healing potion brewed z '{create_earth()}' i '{create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed z '{create_fire()}' i '{create_water()}'"
