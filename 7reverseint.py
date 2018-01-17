class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        j=1
        if x<0:
            x=-x
            j=-1
        temp=x
        newx=0
        while x>0:
            newx=newx*10+x%10
            x=(x-x%10)/10
            if newx>2147483647:
                    return 0
        return newx*j
