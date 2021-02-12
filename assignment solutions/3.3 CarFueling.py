# 3.3 Car Fueling


max_Dist = int(input())
average = int(input())
stops_len = int(input())
stops = input().split()
stops.append(max_Dist)

count = 0
previousStation = 0
currentFuel = average

for i in range(stops_len):
    currentStation = int(stops[i])
    nextStation = int(stops[i+1])
    # check current fuil after traveling previous poin to up to this station
    currentFuel = currentFuel - ( currentStation - previousStation)
    # check reruaird fuil
    requirdFuil = nextStation - currentStation
    if(requirdFuil > average):
        count = -1
        break
    if(requirdFuil > currentFuel):
        currentFuel += average
        count += 1
    # 
    previousStation = currentStation

print(count)
