class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        
        if len(nums) == 1:
            return nums[0]
        else:
            nums.sort()
            for i in range (0,len(nums)-1,2):
                if nums[i] != nums[i+1]:
                    result = nums[i]
                    return nums[i]
                
        if result == 0:
            return nums[-1]
