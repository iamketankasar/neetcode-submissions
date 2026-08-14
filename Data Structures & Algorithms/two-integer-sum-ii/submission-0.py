class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            find = target - i
            if find in numbers and find!=i:
                return [i, find]

        return None