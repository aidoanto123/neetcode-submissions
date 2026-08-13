class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        numbers = {}
        for item in nums:
            if item not in numbers:
                numbers[item] = True
            else:
                output = True
        return output

        