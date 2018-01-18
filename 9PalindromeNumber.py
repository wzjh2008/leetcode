class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i=10
        if x < 0 or (x%i==0 and x/i!=0):
            return False
        inv=0
        while inv < x:
            inv=inv*10+x%i
            if x == inv:
                return True
            x=x/i
        if x == inv:
                return True
        else:
            return False
