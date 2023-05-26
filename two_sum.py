class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_dict = {}
        for i, value in enumerate(nums):
            if target - value in hash_dict:
                return [hash_dict[target - value], i]
            hash_dict[value] = i


print(Solution().twoSum([3, 2, 4], 6))