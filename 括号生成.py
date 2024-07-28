res = []
def backtrack(path, left, right, n):
    if left > n or right > n or left < right:
        return
    if len(path) == 2 * n:
        res.append(path[:])
    backtrack(path + '(', left + 1, right, n)
    backtrack(path + ')', left, right + 1, n)
n = 3
backtrack('', 0, 0, n)
print(res)
