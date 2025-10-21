# nums = [-1,0,1,2,-1,-4]
# nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
nums=[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
output = []
f_set = set()
nums.sort()
# print(nums)
for i in range(0, len(nums)-2):
    j, k =  i + 1, len(nums) - 1

    while(j < k):
        print(i,j,k)
        st = f"{nums[i]}{nums[j]}{nums[k]}"
        if st not in f_set:
            if nums[i] + nums[j] + nums[k] == 0:
                output.append([nums[i], nums[j], nums[k]])
                f_set.add(st)
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1

        else:
            j += 1
            k -= 1
print(output, "set is : ",f_set)
