class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = [ord(x) for x in s]
        seen2 = [ord(x) for x in t]
        return sorted(seen1) == sorted(seen2)
        