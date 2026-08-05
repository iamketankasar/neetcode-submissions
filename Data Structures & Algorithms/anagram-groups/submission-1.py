from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        compare_dict = defaultdict(list)
        final_res = []

        for s1 in strs:
            ascii_value = "$".join(str(ord(c)) for c in sorted(s1))
            compare_dict[ascii_value].append(s1)
        
        for value in compare_dict.values():
            final_res.append(value)
        return final_res
