class Solution:
    def minimumSum(self, num: int) -> int:
        n = list()
        for i in str(num):
            n.append(i)
        n.sort()
        return int(n[0])*10 + int(n[1])*10 + int(n[2]) + int(n[3])    