class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        _min = float("inf")
        _sum = 0
        for r in range(0,len(nums)):
            _sum += nums[r]
            
            while _sum >= target:
                _min = min(r-l + 1,_min)
                l += 1 
                _sum -= nums[l-1]
            
        return _min if not _min == float("inf") else 0
        