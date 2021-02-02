lass Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            a = target - nums[i]
            if a in nums[:i] or a in nums[i+1:]:
                nums.pop(i)
                return [i,nums.index(a)+1]
