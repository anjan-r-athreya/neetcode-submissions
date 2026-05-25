class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        ptr1 = 0
        ptr2 = n - 1
    
        while ptr1 < ptr2:
            while ptr1 < ptr2 and s[ptr1].isalnum() == False:
                ptr1 = ptr1 + 1
            while ptr1 < ptr2 and s[ptr2].isalnum() == False:
                ptr2 = ptr2 - 1
            
            if s[ptr1].lower() != s[ptr2].lower():
                return False
            elif s[ptr1].lower() == s[ptr2].lower():
                ptr1 = ptr1 + 1
                ptr2 = ptr2 - 1
            
        return True