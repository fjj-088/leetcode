res = []
path = []
def backtrack(nums, visited):
    if len(path) == len(nums):
        res.append(path[:])
        return
    # res.append(path[:])
    for i in range(len(nums)):
        # 当前与上一个值相同，且前一个还没被访问，说明同一数层上有两个相同元素，同数层前一位重复读取了，如果不加这个条件(上一个已经被访问)，那肯定全continue了，因为数组里一定有相同的
        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
            continue
        if not visited[i]:
            # print('-')
            visited[i] = True
            path.append(nums[i])
            backtrack(nums, visited)
            path.pop()
            visited[i] = False
nums=[1,2,2]
nums.sort()
visited = [False] * len(nums)
backtrack(nums, visited)
print(res)