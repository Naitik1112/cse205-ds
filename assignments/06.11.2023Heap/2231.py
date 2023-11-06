class Solution:
    def largestInteger(self, num: int) -> int:
        res = int()
        odd = list()
        even = list()
        num = str(num)
        for i in num:
            if int(i)%2 == 0:
                even.append(int(i))
            else:
                odd.append(int(i))
        odd.sort()
        even.sort()

        for i in num:
            if int(i)%2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res                          