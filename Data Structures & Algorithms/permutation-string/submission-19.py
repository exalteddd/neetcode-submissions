class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        valid = {}
        for char in s1:
            if char in valid:
                valid[char] += 1
            else:
                valid[char] = 1
        length = len(s1)


        for l in range(len(s2)):
            found = {}
            r = l
            while r < l + length and r < len(s2):
                if s2[r] in found:
                    found[s2[r]] += 1
                else:
                    found[s2[r]] = 1
                r += 1
            if found == valid:
                print(l)
                return True
        return False







        

        