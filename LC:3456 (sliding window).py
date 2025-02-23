class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n=len(s)
        if k>len(s):#use sliding window technique
            return False
        for i in range(n-k+1):#define everything in numbers and st them to string as indexes imp*****
            substring=s[i:i+k]#substring set using defined numbers of loop

            if len(set(substring)) != 1:#check if all elements are same
                continue
            if i>0 and substring[0]==s[i-1]:# check if previous element of substring is same
                continue
            if i<n-k and substring[0]==s[i+k]:# check if nect element afte rsubstring is same
                continue
            return True
        return False
