import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        rev=ch[::-1]
        if ch==rev:
            return True
        else:
            return False
        