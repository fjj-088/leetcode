res = []
path = []
def backtrack(n, k, index):
    if len(path) > k or sum(path) > n:
        return
    if sum(path) == n and len(path) == k:
        res.append(path[:])
        return
    for i in range(index, 10):
        path.append(i)
        backtrack(n, k, i + 1)
        path.pop()
k = 3
n = 7
backtrack(n, k, 1)
print(res)