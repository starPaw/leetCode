class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                                "CCCC").replace(
            "CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))


class Solution2:
    def romanToInt(self, s: str) -> int:
        storeKeyValue = {}
        storeKeyValue['I'] = 1
        storeKeyValue['V'] = 5
        storeKeyValue['X'] = 10
        storeKeyValue['L'] = 50
        storeKeyValue['C'] = 100
        storeKeyValue['D'] = 500
        storeKeyValue['M'] = 1000
        s = s[::-1]
        integer = 0
        integer += storeKeyValue[s[0]]
        for i in range(1, len(s)):
            if storeKeyValue[s[i]] >= storeKeyValue[s[i - 1]]:
                integer += storeKeyValue[s[i]]
            else:
                integer -= storeKeyValue[s[i]]
        return integer


a = Solution2().romanToInt("efwfe")
