from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)
        res_list = []
        # nums = sorted(nums)
        for num in nums:
            result[num].append(num)

        for key,value in result.items():
            if len(value)>= k:
                res_list.append(key)
            
        return res_list