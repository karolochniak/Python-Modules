import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("At the beginning of the game, your inventory is usually")
        print("empty ;)")
        return

    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(':')
        item_name = parts[0]
        item_qty = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            inventory[item_name] = int(item_qty)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    sum_sztuk = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {sum_sztuk}")

    for item, qty in inventory.items():
        procent = (qty / sum_sztuk) * 100
        print(f"Item {item} represents {round(procent, 1)}%")

    most_item = max(inventory, key=lambda k: inventory[k])
    least_item = min(inventory, key=lambda k: inventory[k])

    print(f"Item most abundant: {most_item} "
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} "
          f"with quantity {inventory[least_item]}")

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
