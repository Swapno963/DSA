numbers = [2, 3, 4]
target = 6

# i = 0
j = 1
nums = []
for i in range(len(numbers) - 1):
    j = i + 1
    while j < len(numbers):
        if numbers[i] + numbers[j] == target:
            nums.append(i + 1)
            nums.append(j + 1)
            break

        else:
            j += 1
print(nums)
