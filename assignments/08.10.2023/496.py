class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res  = []
        for i in range (len(nums1)):

            index = nums2.index(nums1[i])
            number = nums2[index]

            for i1 in range (index+1,len(nums2)):
                if nums2[i1] > number:
                    res.append(nums2[i1])
                    break
            if len(res) != i + 1:
                res.append(-1)

        return  res                             

