# height = [1, 7, 2, 5, 4, 7, 3, 6]
height = [2, 2, 2]
# start from 0 to len -1
l = 0
r = len(height) - 1
max_area = 0

for _ in range(len(height)):
    # Calculate the area
    area = min(height[l], height[r]) * (r - l)
    max_area = max(max_area, area)

    #  move pointer
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(max_area)
