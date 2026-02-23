class Solution:
    def isHappy(self, n: int) -> bool:
        keep = {}
        keep[0] = None

        _sum = 0
        while n not in keep:
            keep[n] = None
            while n > 0:
                _sum += (n % 10) ** 2
                n //= 10

            if _sum == 1:
                return True

            n = _sum
            _sum = 0
        return False
        
        