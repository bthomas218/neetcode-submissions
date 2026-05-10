from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        heap = [(v, k) for k, v in freq_map.items()]

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [h[1] for h in heap]