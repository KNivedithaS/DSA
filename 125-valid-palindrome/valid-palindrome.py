class Solution(object):
    def isPalindrome(self, s):
        st="".join(char.lower() for char in s if char.isalnum())
        if st[::-1]==st[::]:
            return True
        return False