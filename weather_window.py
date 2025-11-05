"""
HW04 — Weather Window: Sliding Maximum
"""

import heapq

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]

    heap = []  # max heap simulated with (-value, index)
    result = []

    for i, num in enumerate(nums):
        # Push current element as (-value, index)
        heapq.heappush(heap, (-num, i))

        # Remove elements out of current window (index <= i - k)
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)

        # Once we’ve processed at least k elements, record the max
        if i >= k - 1:
            result.append(-heap[0][0])

    return result
