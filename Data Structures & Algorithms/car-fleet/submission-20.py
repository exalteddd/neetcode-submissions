class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        time = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
            
        pairs.sort(key = lambda x:x[0])
        for i in range(len(position)):
            time.append((target - pairs[i][0])/pairs[i][1])
        # print(time)

        q = len(time) - 1
        
        while q > 0:
            if time[q] >= time[q-1]:
                time.pop(q-1)
            q-= 1
        return len(time)
        



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
        
