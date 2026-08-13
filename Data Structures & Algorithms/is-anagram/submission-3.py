class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}

        s = tuple(sorted(s))
        t = tuple(sorted(t))

        word[s] = True

        if t in word:
            return True
        return False
