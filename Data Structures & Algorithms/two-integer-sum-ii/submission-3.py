class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Map = {}
        for i, n in enumerate(numbers):
            number = target - n
            if number in Map:
                return [Map[number] + 1, i + 1]
            else:
                Map[n] = i
        