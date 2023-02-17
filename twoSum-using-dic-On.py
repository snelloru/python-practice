def twoSum(nums, target):
    sum={}
    for index, num in enumerate(nums):
        if target - num in sum:
            return [index, sum[target - num]]
        else:
            sum[num] = index


print(twoSum([2,7,11,15], 9))
print(twoSum([1,7,2,15], 9))
print(twoSum([3,3],6))
