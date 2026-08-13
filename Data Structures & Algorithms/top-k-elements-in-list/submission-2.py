class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        result = []
        answer = []

        for num in nums:
            if num not in numbers:
                numbers[num] = 1              
            numbers[num] += 1
                
        for num, count in numbers.items():
            result.append([count, num])
        result.sort()

        while k > 0:
            answer.append(result.pop()[1])
            k -= 1
        return answer

        