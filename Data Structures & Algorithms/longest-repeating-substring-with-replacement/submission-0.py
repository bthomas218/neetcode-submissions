from collections import Counter 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = Counter()
        most_common = 0
        res = 0

        l = 0 
        for r in range(len(s)):
            count[s[r]] += 1
            most_common = max(most_common, count[s[r]])

            while (r - l + 1) - most_common > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res

        