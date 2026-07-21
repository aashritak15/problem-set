class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(s_new) - 1

        for i in range(len(s_new)):
            if s_new[left] == s_new[right]:
                left +=1 
                right -= 1 
                i+=1
            else:
                return False 

        return True 
        