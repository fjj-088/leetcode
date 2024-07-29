import heapq
nums = [3,2,1,5,6,4]
k = 2
heap = heaqp.heapfy
for num in nums:
    if len(heap) == k:
        if num > heap[k]:
            heap.heapqpush(num)
    else:
        heap.heapqpush(num)
print(heap[k])
