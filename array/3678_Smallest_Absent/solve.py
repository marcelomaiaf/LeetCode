class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = max(sum(nums) // len(nums) + 1, 1)

        while avg in nums:
            avg += 1
        return avg
        
