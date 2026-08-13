class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for item in strs:
            s_i = "".join(sorted(item))
            res[s_i].append(item)
        return list(res.values())


        