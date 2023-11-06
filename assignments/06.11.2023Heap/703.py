class KthLargest:
     
    def __init__(self, k: int, nums: List[int]):
        self.main_list = nums
        self.kth = k

    def add(self, val: int) -> int:
        self.main_list.append(val)
        self.main_list.sort()
        if len(self.main_list) >= self.kth:
            return self.main_list[-self.kth]  
        else:
            return 0          


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)