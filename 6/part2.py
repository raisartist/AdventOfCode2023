input = {
    "time": 34908986,
    "distance": 204171312101780
}

answer = 1

ways_to_win = 0
holding_time = 0
travel_time = 0
travel_distance = 0

while holding_time < input["time"]:
    holding_time += 1
    travel_time = input["time"] - holding_time
    travel_distance = holding_time * travel_time

    # print(f"pressing {holding_time} ms, traveling {travel_time} ms, dinstance {travel_distance} mm")

    if travel_distance > input["distance"]:
        # print("It's a new record!")
        ways_to_win += 1

answer *= ways_to_win

print(answer)