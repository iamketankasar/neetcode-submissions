import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        size = len(result)

        for i in range(0, size//2):
            if result[i]==result[size-i-1]:
                continue
            else:
                return False
        
        return True
        