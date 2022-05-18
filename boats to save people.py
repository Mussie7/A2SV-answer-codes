class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:  
            if people[r] + people[l] > limit:
                r -= 1
                boat += 1
            else:
                r -= 1
                l += 1
                boat += 1
        
        return boat
