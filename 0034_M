class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        # Solution 1: While this solution is very simple and readable, it has time complexity O(n) i.e. 
        # run time scales linearly with input. See Solution 2 for how to achieve O(log(n)) time complexity.
        
        hit = []                     # The hit list will keep track of all indices where nums contains
        result = []                  # ('hits') our target value.
        
        for i in range (len(nums)):  # *search method* Ex: Input nums=[1,2,3,3,3,5], target=3
            if nums[i] == target:    # nums[i] == 3 at i==2, i==3, and i==4, so hit=[2,3,4]
                hit.append(i)
                
        if len(hit) == 0:            # If no indices hit our target value, the target value is not in 
            return [-1,-1]           # nums, so return [-1,-1]
        
        elif len(hit) == 1:          # If the target value only occurs at one index, then its position
            hit.append(hit[0])       # both starts and ends at that index, so return [hit[0],hit[0]]
            return hit
        
        else:                        # If the target value occurs in at least two indices, the start
            result.append(hit[0])    # position is the first index it occured and the end position is 
            result.append(hit[-1])   # the last, so return [hit[0],hit[-1]]
            return result
        
        # Solution 2: We can improve our time complexity to O(log(n)) by restructuing the search method
        # using bisection (called binary search method). This will allow python to find the target
        # integer efficiently for large inputs.
        
        start=1                        # Initialize the output for start and end indices. I set start > end so that 
        end=0                          # if no new start or end indices are found (meaning target not in array), I 
                                       # can return [-1,1] via *if start > end*
        high = len(nums)-1             
        low = 0 
        
        while (low <= high):
            mid = (high + low) // 2    
            if nums[mid] == target:    
                start = mid
                high = mid-1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        high = len(nums)-1
        low = 0
                
        while (low <= high):
            mid = (high + low) // 2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        if end >= start:
            return [start,end]
        else:
            return[-1,-1]
