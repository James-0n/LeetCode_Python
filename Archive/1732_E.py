class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt=0
        alt=0
        for i in range (len(gain)):
            alt+=gain[i]
            if alt > maxAlt:
                maxAlt=alt
        return maxAlt
        
