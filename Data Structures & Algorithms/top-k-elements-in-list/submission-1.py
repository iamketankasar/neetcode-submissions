from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)
        res_list = []
        # nums = sorted(nums)
        for num in nums:
            result[num].append(num)

        res_list = sorted(
            result,key=lambda key: len(result[key]),
            reverse=True
            )[:k]

            
        return res_list