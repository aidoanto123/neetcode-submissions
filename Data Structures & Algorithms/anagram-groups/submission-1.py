class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        result = []

        for word in strs:
            new_word = tuple(sorted(word))
            words[new_word].append(word)
        
        for v in words.values():
            result.append(v)
        
        return result


        