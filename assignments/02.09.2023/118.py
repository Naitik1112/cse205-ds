class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        List = [""]
        def recu(i = 0 , List = [ ] ):
            if i == numRows :
                return
            if i == 0:
                List[0] = ([1]) 

            for i1 in range (0,i):
                print("i1 : " + str(i1) + " i : " + str(i)) 
                if i1 == 0 :
                    List.append([1])
                if i1 == i - 1 :
                    List[i-1].append(1)
                else :
                    List[i-1].append("")
            
            for i1 in range (1,i):
                List[i-1][i1] = List[i-2][i1] + List[i-2][i1-1]
            
            recu(i+1,List)
        
        recu(0,List)

        Last = List.pop()
        List.insert(0,Last)
        return List


