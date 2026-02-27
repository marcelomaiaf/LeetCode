class Solution:
    def reverseWords(self, s: str) -> str:
        _arr = s.strip().split()
        l,r = 0, len(_arr) - 1
        res = ""
        while l < r: 
            _arr[l], _arr[r] = _arr[r],_arr[l]
            l += 1
            r -= 1
        
        for i in range(len(_arr)):
            if i < len(_arr) - 1:
                res += _arr[i] + " "
            else:
                res += _arr[i]
        return res