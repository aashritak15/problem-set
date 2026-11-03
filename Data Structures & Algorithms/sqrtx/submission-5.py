class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x 
        ans = 0

        while r >= l:
            m = (l + r) // 2

            if (m ** 2) <= x:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
        