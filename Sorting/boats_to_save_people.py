# people = [5,1,4,2] 
# limit = 6

people = [1,3,2,3,2]
limit = 3
people.sort()
print(people)
j,k = 0, len(people)-1
count = 0
while(j <= k):
    print(j , " ", k)
    if j == k:
        count += 1 
        break
    if people[j] + people[k] <= limit:
        count += 1
        j += 1
        k -= 1
    elif people[j] + people[k] > limit:
        k -= 1
        count += 1    
print(count)
        