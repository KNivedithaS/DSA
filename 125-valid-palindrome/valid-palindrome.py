class Solution(object):
    def isPalindrome(self, s):
        st="".join(char.lower() for char in s if char.isalnum())
        j=len(st)-1
        for i in range(len(st)//2):
            if st[i]==st[j]:
                j-=1
            else:
                return False
        return True