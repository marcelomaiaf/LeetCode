class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        _dict = {} 
        _max = 1
        nums.sort()
        for i in nums:
            _dict[i + 1] = _dict.get(i,0) + 1
            _max = max(_dict[i + 1],_max)


        return _max
