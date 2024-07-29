res = []
path = []
def backtrack(nums, index):
    res.append(path[:])
    # if index >= len(nums):
    #     return
    for i in range(index, len(nums)):
        path.append(nums[i])
        backtrack(nums, i + 1)
        path.pop()
backtrack([1,2,3], 0)
print(res)