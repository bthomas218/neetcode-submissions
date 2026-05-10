from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            anagrams[tuple(key)].append(s)
        
        return [v for v in anagrams.values()]