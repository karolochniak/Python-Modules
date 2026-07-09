def recursion(day):
    if day == 0:
        return
    recursion(day - 1)
    print("Day " + str(day))
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursion(days)
    print("Harvest time!")
