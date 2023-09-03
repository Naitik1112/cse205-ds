class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        list1 = ''
        
        for i in word1 :
            list1 = list1 + i

        
        list2 = ''

        for i1 in word2:
            list2 = list2 + i1

       

        if list1 == list2 :
            return True
        else :
            return False
