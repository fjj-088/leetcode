res = []
path = []
def backtrack(n, k, index):
    if len(path) == k:
        res.append(path[:])
        return
    for i in range(index, n + 1):
        path.append(i)
        backtrack(n, k, i + 1)
        path.pop()
backtrack(4,2,1)
print(res)