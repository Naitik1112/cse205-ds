class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ops = operations
        for i in ops:
            if i != "+" and i != "C" and i != "D" :
                res.append(int(i))
            elif i == "+":
                res.append(int(res[-1]+res[-2]))
            elif i == "C":
                res.pop()
            elif i == "D":
                res.append(int(res[-1]*2))
        return sum(res)

        