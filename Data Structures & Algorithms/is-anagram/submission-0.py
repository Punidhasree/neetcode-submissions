class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s={}
        hash_t={}
        for i in s:
            if i not in hash_s:
                hash_s[i]=i
            else:
                hash_s[i]=1

        for i in t:
            if i not in hash_t:
                hash_t[i]=i
            else:
                hash_t[i]=1
        if hash_s==hash_t:
            return True
        else:
            return False

