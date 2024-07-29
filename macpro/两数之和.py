nums = [3,2,4]
target = 6
hash_map = dict()
size = len(nums)
for i in range(size):
    if target - nums[i] in hash_map:
        print(hash_map[target - nums[i]], i)
    hash_map[nums[i]] = i
