input = [
    {
        "time": 34,
        "distance": 204
    },
    {
        "time": 90,
        "distance": 1713
    },
    {
        "time": 89,
        "distance": 1210
    },
    {
        "time": 86,
        "distance": 1780
    },
]

# input = [
#     {
#         "time": 7,
#         "distance": 9
#     },
#     {
#         "time": 15,
#         "distance": 40
#     },
#     {
#         "time": 30,
#         "distance": 200
#     },
# ]



answer = 1

for data in input:

    ways_to_win = 0
    holding_time = 0
    travel_time = 0
    travel_distance = 0

    while holding_time < data["time"]:
        holding_time += 1
        travel_time = data["time"] - holding_time
        travel_distance = holding_time * travel_time

        # print(f"pressing {holding_time} ms, traveling {travel_time} ms, dinstance {travel_distance} mm")

        if travel_distance > data["distance"]:
            # print("It's a new record!")
            ways_to_win += 1

    answer *= ways_to_win

print(answer)