class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = []

        for item in nums:
            if item not in test:
                test.append(item)
            else:
                return True
        return False
        