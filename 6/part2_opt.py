import time
import math
start_time = time.time()

input = {
    "time": 34908986,
    "distance": 204171312101780
}

#quadratic equasion formula!

holding_time = 1 #a
race_time = input["time"] #b
distance = input["distance"] #c

# travel_distance = holding_time * (race_time - holding_time)
# -holding_time**2 + holding_time*race_time - travel_distance = 0

min_value = math.ceil(((0 - race_time) + math.sqrt(race_time**2 - 4*holding_time*distance))/-2)

max_value = math.floor(((0 - race_time) - math.sqrt(race_time**2 - 4*holding_time*distance))/-2)

print(max_value - min_value + 1)
print(f"runtime: {time.time()-start_time}")
# runtime: 0.00045299530029296875