class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {} # sorted_word : []
        for word in strs:
            strn = "".join(sorted(word))
            if strn not in dict1:
                dict1[strn] = [word]
            else:
                dict1[strn].append(word)
        result = []
        for item in dict1:
            result.append(dict1[item])
        return result

        