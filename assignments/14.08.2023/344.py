class Solution:

    def reverseString(self, s: List[str], i = 0 ) -> None:
       
        if i == len(s)//2: 
             return

        s[len(s) - i - 1 ],s[i] = s[i] , s[len(s)-i-1]

        self.reverseString(s,i+1)
        return list