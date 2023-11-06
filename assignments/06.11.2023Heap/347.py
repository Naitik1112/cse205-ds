class Solution(object):
    def topKFrequent(self, nums, k):
         
        m = {}
        r = []
        for i in nums:
            if i in m :
                m[i]+= 1
            else:
                m[i] = 1 

        for _ in range (k):
            max_freq = 0
            max_nums = 0
            for key,value in m.items():
                if value > max_freq:
                    max_freq = value
                    max_nums = key
            r.append(max_nums)
            m.pop(max_nums)
        return r            

        