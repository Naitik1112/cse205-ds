class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        part2 = list()
        part1 = list()
        for i in range (len(arr2)):
            count = 0
            for j in range (len(arr1)):
                print(arr1[j]," " ,i)
                if arr1[j] == arr2[i]:
                    count+=1
                if arr1[j] not in arr2:
                    n = arr1.pop(j)
                    part2.append(n)
                if len(arr1) - 2 < j :
                    break  
                                            
            sub = [arr2[i]]*count
            part1.extend(sub)
            
        part2.sort()
        part1.extend(part2)
        return part1
        