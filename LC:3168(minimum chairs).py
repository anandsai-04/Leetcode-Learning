class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        You are given a string s. Simulate events at each second i:

If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.
        """
        n=0#n is occupancy initially it is none so ZERO
        j=[]
        for i in range(len(s)):
            if s[i]=="E":#we want to find max occupancy
                n+=1
                j.append(n)
            elif s[i]=="L":#L is leaving the chair, E is Sitting in the chair
                n-=1
                j.append(n)
            else:
                n+=0
                j.append(n)
        
        return max(j)
