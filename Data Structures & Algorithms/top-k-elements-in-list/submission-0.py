class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1) ]
        count = {}


        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            buckets[cnt].append(num)
        
        results = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results