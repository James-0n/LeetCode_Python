class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen=0
        result=0
        for i in range (len(rectangles)):
            if min(rectangles[i]) > maxLen:
                maxLen=min(rectangles[i])
        for x in range (len(rectangles)):
            if min(rectangles[x])==maxLen:
                result=result+1   
        return result
                
