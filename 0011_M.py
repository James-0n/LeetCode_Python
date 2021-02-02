# Question: Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

# Solution 1: Here's how you would go about a brute force solution to the problem. It has O(n^2) time complexity. 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_Vol=0;
        
        for i in range (len(height)):
            for j in range (i+1,len(height)):
                Volume=min(height[i],height[j])*(j-i)
                
                if Volume > max_Vol:
                    max_Vol=Volume
                    
        return max_Vol
        
# Solution 2: We can achieve O(n) time complexity by using the two pointers method. Our two pointers i and j will represent our left and
# right boundaries, respectively. 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        i , j = 0 , len(height)-1
        
        while (i < j):
                
            A = min(height[j],height[i])*(j-i)
            
            if A > maxA:
                maxA=A
                
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        
        return maxA
        
        
        
