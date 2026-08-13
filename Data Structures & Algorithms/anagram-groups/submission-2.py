class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)
        for item in strs:
            sort = "".join(sorted(item))
            if sort not in di:
                di[sort].append(item)
            else:
                di[sort].append(item)
        ans = []
        for v in di.values():
            ans.append(v)
        return ans

