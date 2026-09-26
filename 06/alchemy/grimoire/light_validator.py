from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    if any(ing.lower() in ingredients_lower for ing in allowed):
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
