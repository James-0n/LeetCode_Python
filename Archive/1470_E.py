class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        result=[]
        
        while (i < n):
            for j in range (i,2*n,n):
                result.append(nums[j])
            i+=1
        return result
        
