class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_items[:k]]