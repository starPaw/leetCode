class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r, v in enumerate(s):

            if v not in seen:
                output = max(output, r - l + 1)
            else:
                if seen[v] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[v] + 1
            seen[v] = r
        return output


