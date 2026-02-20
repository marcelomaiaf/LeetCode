class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)
        if n[0] == "-":
            for i in range(1,len(n)):
                if n[i] > x:
                    return n[:i] + f"{x}" + n[i:]
            return n + f"{x}"

        else: 
            for i in range(len(n)):
                if n[i] < x:
                    return n[:i] + f"{x}" + n[i:]
            return n + f"{x}"

        