def elevator(floors_to_visit):
    SINGLE_FLOOR_TRAVEL_TIME = 10
    travel_time = 0
    total_floors_traveled = 0
    floors_visited = ""

    for i in range(len(floors_to_visit)):
        # If there is another floor to travel to
        if i != len(floors_to_visit) - 1:
            # Find the absolute difference with next value
            total_floors_traveled += abs(floors_to_visit[i] - floors_to_visit[i+1])
        
        if floors_visited:
            floors_visited += ", "

        # Add floor to floors_visited string
        floors_visited += str(floors_to_visit[i])

    travel_time = SINGLE_FLOOR_TRAVEL_TIME * total_floors_traveled
    return "{0} {1}".format(travel_time, floors_visited)

def main():
    print(elevator([12, 2, 9, 1, 32]))
    print(elevator([12]))
    print(elevator([]))
    return

if __name__ == "__main__":
    main()