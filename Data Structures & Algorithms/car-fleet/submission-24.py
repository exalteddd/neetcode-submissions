class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        time = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pairs.append((position[i],speed[i],time))
            
        pairs.sort(key = lambda x:x[0])
         # exacxt number of steps not in decimal
        # print(time)

        q = len(pairs) - 1
        
        while q > 0:
            if pairs[q][2] >= pairs[q-1][2]:
                pairs.pop(q-1)
            q-= 1
        return len(pairs)
        



        # [1, 2, 3, 4, 5]
        # [1, 2, 3, 4, 5]
        # [2, 3, 4, 5]
        #[2, 4, 5]
        # 10-4 = 6/2 = 3
        #[ 3,5,10,3]
        # [3,3,5,10]
        # [3,5,10]
        # [4, 1, 0, 7]
        # [0, 1, 4, 7]
        # 10, 50
        # 0, 200
        
