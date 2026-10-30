class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mp = {}
        max_length = 0

        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]] + 1)
            mp[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length