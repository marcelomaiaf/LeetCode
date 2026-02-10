class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = _max = 0
        
        if len(s) == 0:
            return 0

        for r in range(0,len(s)):
            while s[r] in s[l:r]:
                l += 1
            _max = max(_max, r - l + 1)

        return _max
        
        