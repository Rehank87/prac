from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for k,v in enumerate(nums):
            # print(k)
            print(f"v {v}")
            diff = target - v
            print(f"diff {diff}")
            if diff in dict.values():
                return [nums.index(diff), k]
            else:
                dict[k] = v
                print(dict)

nums = [3,2,4]
target = 6
solver = Solution()
result = solver.twoSum(nums=nums, target=target)
print(result)