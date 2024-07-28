res = []
path = []
def backtrack(nums, index, visited):
    res.append(path[:])
    # if index >= len(nums):
    #     return
    for i in range(index, len(nums)):
        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
            continue
        visited[i] = True
        path.append(nums[i])
        backtrack(nums, i + 1, visited)
        path.pop()
        visited[i] = False
nums = [1,1,1]
nums.sort()
visited = [False] * len(nums)
backtrack(nums, 0, visited)
print(res)