class Solution:
    def frequencySort(self, s: str) -> str:
        sub1 = list()
        sub2 = list()
        for i in s:
            if i not in sub2:
                sub2.append(i)
                sub1.append(1)
            else:  
                sub1[sub2.index(i)] += 1 
        sub3 = list()
        for i in range (len(sub2)):
            sub4 = sub2[i]*sub1[i]
            sub4 = ''.join(sub4)
            sub3.append(sub4)  
        sub3.sort(key=lambda x: len(x) , reverse = True)
        return ''.join(sub3)                