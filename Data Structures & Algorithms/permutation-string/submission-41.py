class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        valid = {}
        for char in s1:
            valid[char] = valid.get(char, 0) + 1

        length = len(s1)
        found = {}
        for char in s2[:length]:
            found[char] = found.get(char, 0) + 1

        l = 0
        r = length - 1

        while r < len(s2) - 1:
            if found == valid:
                return True

            found[s2[l]] -= 1
            if found[s2[l]] == 0:
                found.pop(s2[l])

            l += 1
            r += 1

            # Add the character entering the window.
            found[s2[r]] = found.get(s2[r], 0) + 1

        return found == valid