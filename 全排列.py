# res = []
# path = []
# def backtrack(nums):
#     if len(path) == len(nums):
#         res.append(path[:])
#         return
#     for num in nums:
#         if num not in path:
#             path.append(num)
#             backtrack(nums)
#             path.pop()
# def backtrack(nums):
#     if len(path) == len(nums):
#         res.append(path[:])
#         return
#     for i in range(len(nums)):
#         if nums[i] not in path:
#             path.append(nums[i])
#             backtrack(nums)
#             path.pop()
# backtrack(nums=[1,2,3])
# print(res)

res = []
path = []
def backtrack(nums, visited):
    if len(path) == len(nums):
        res.append(path[:])
        return
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            backtrack(nums, visited)
            path.pop()
            visited[i] = False
nums=[1,2,3]
visited = [False] * len(nums)
backtrack(nums, visited)
print(res)