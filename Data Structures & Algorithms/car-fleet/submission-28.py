class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pairs.append((position[i],speed[i],time))
            
        pairs.sort(key = lambda x:x[0])
        # idea is to count the time each car takes to get to target. sort the cars by last to first. given car a in front of car b. if time of car a less than time of car b then it must collide and pop car a, which is important

        q = len(pairs) - 1
        
        while q > 0:
            if pairs[q][2] >= pairs[q-1][2]:
                pairs.pop(q-1)
            q-= 1
        return len(pairs)
        
