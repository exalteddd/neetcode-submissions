class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        data = [[0,temperatures[0]]]

        for i in range(1,len(temperatures)):
            while len(data) > 0 and temperatures[i] > data[-1][1]:
                index = data[-1][0]
                result[index] = i - index
                data.pop()
            data.append([i,temperatures[i]])
        return result


        
        
