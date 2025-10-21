# people = [5, 1, 4, 2]
# limit = 6
people = [1, 3, 2, 3, 2]
limit = 3

dc = {}
boat = 0
for item in people:
    diff = limit - item
    if diff == 0:
        boat += 1
    else:
        dc[item] = limit - item


for key, value in dc.items():
    if value in dc and dc[value] != -1:
        boat += 1
        dc[value] = -1
        dc[key] = -1
# dc[key] = -1
print(dc)
print(boat)
