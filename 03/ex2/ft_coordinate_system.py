import math


def get_player_pos() -> tuple:
    while True:
        point = input("Enter new coordinates as floats in format 'x,y,z':")
        points = point.split(',')
        if (len(points) != 3):
            print("Invalid syntax")
            continue
        cords = []
        error = False
        for i in points:
            try:
                cords.append(float(i))
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                error = True
                break
        if not error:
            return (cords[0], cords[1], cords[2])


def calc_sqrt(p1: tuple, p2: tuple) -> float:
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 +
                     (p2[2] - p1[2])**2)


def main() -> None:
    print("=== Game Coordinate System === \n")
    print("Enter a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance1 = calc_sqrt((0, 0, 0), pos1)
    print(f"Distance to center: {round(distance1, 4)} \n")
    print("Enter a second set of coordinates")
    pos2 = get_player_pos()
    distance2 = calc_sqrt(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {round(distance2, 4)}")


if __name__ == "__main__":
    main()
