class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0,len(s) -1
        
        while l < r: # standard 2 ptr loop
            while l < r and not s[l].isalnum(): # skip non alphanumerics
                l+=1
            while l < r and not s[r].isalnum(): # skip non alphanumerics
                r-=1    
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
