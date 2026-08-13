class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = []
        for row in matrix:
            for ch in row:
                ans.append(ch)
        return target in ans