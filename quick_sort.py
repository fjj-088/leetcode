# https://www.bilibili.com/video/BV11P4y1R7WT/?spm_id_from=333.999.0.0&vd_source=dda7049fc1235b4e55a2697ca7a23a15
# 快速排序
def quickSort(arr: [int], low: int, high: int):
    left = low
    right = high

    if left >= right:
        return
    p = arr[left]
    while left < right:
        while left < right and arr[right] >= p:
            right -= 1
        if(arr[right] < p):
            arr[left] = arr[right]

        while left < right and arr[left] <= p:
            left += 1
        if arr[left] > p:
            arr[right] = arr[left]

        if left == right:
            arr[left] = p # 把p再放回去

        quickSort(arr, low, right - 1)  # 递归左子树
        quickSort(arr, right + 1, high)  # 递归右子树

arr = [2,3,4,1,2,4,7,6]
print(arr)
quickSort(arr, 0, len(arr) - 1)
print(arr)