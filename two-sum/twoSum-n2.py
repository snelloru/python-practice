def twoSum(nums, target):
        for i in range(len(nums)-1):
            print(i)
            for j in range(i+1, len(nums)):
                print(j)
                if nums[i] + nums[j] == target:
                    return [i,j]

                  
                  

print(twoSum([2,7,11,15], 9))
print(twoSum([1,7,2,15], 9))
print(twoSum([3,3],6))
