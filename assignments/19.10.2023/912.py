class Solution:
    buf = [0] * 50000
    def sortArray(self, nums: List[int], lo=0, hi=None) -> List[int]:
        hi = len(nums) if hi is None else hi
        n = hi - lo
        if n == 1:
            return nums
        if n == 2:
            if nums[lo] > nums[hi-1]:
                nums[lo], nums[hi-1] = nums[hi-1], nums[lo]
                return nums
        half = (lo + hi) // 2
        self.sortArray(nums, lo=lo, hi=half)
        self.sortArray(nums, lo=half, hi=hi)
        buf = self.buf
        i = 0
        a = lo
        b = half
        while a < half and b < hi:
            if nums[a] <= nums[b]:
                buf[i] = nums[a]
                a += 1
            else:
                buf[i] = nums[b]
                b += 1
            i += 1
        while a < half:
            buf[i] = nums[a]
            a += 1
            i += 1
        while b < hi:
            buf[i] = nums[b]
            b += 1
            i += 1
        nums[lo:hi] = buf[:n]
        return nums