def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(
            seed_type.capitalize() + " seeds: " +
            str(quantity) + " " + unit + " available")
    else:
        if unit == "grams":
            print(
                seed_type.capitalize() + " seeds: " +
                str(quantity) + " " + unit + " total")
        else:
            if unit == "area":
                print(
                    seed_type.capitalize() + " seeds: " + "covers " +
                    str(quantity) + " square meters")
            else:
                print("Unknown unit type")
