class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        size = len(needle)
        while i < len(haystack) - size + 1:
            if needle == haystack[i:i+size]:
                return i
            i += 1
        return -1