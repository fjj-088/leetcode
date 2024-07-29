res = []
path = []
def backtrack(nums, target ,index):
    if sum(path) > target:
        return
    if(sum(path) == target):
        res.append(path[:])
        return
    for i in range(index, len(nums)):
        path.append(nums[i])
        backtrack(nums, target, i)
        path.pop()

candidates = [2,3,6,7]
target = 7
backtrack(candidates, target, 0)
print(res)