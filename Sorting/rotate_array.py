nums = [1000,2,4,-3]
k = 21


while k > 0:
    end = nums[-1]
    nums.pop()
    nums.insert(0,end)

    k -= 1
print(nums)