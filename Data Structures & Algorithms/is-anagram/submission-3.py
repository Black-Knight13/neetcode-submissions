class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {} # create 2 hashmaps

        if len(s) != len(t): # if the input strings aren't the same length automatically false
            return False

        for i in range(len(s)):  # iterate through len & add each occurance to map
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        return hash_s == hash_t    # boolean compare maps

        