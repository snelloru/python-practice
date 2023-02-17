def uniqueOccurrences(arr):
    occur_list = []
    for i in set(arr):
        occur_list.append(arr.count(i))
    return len(occur_list) == len(set(occur_list))


print(uniqueOccurrences([1,1,2,2,2,3,3,3,3]))
print(uniqueOccurrences([1,1,2,2,3,3,3]))
