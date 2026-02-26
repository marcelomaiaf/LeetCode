class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        keep = {}

        for i in range(len(s)):
            if s[i] in keep:
                if keep.get(s[i]) != t[i]:
                    return False
            else:
                if t[i] in t[:i]:
                    return False
                keep[s[i]] = t[i]
        return True
        