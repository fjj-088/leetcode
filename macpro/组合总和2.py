res = []
path = []
def backtrack(nums, target ,index, visited):
    if sum(path) > target:
        return
    if(sum(path) == target):
        res.append(path[:])
        return
    for i in range(index, len(nums)):
        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
            continue
        path.append(nums[i])
        visited[i] = True
        backtrack(nums, target, i + 1, visited)
        visited[i] = False
        path.pop()

candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
visited = [False] * len(candidates)
backtrack(candidates, target, 0, visited)
print(res)