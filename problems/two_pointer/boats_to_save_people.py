# people = [5, 1, 4, 2]
# limit = 6

people = [1, 3, 2, 3, 2]
limit = 3
count = 0
for i in range(len(people)):
    people[i] = limit - people[i]


print(people)
