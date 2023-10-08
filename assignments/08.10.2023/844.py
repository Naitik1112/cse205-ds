class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def check(Compare):
            res = []
            for i in Compare:
                if i != "#":
                    res.append(i)
                elif len(res) != 0:
                    res.pop()
            return res

        if check(s) == check(t):
            return True
        else:
            return False

          

        