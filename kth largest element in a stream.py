class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums[len(nums)-k:] if k < len(nums) else nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            i = len(self.nums) - 1
            while i > 0:
                if self.nums[i] < self.nums[(i-1)//2]:
                    self.nums[i], self.nums[(i-1)//2] = self.nums[(i-1)//2], self.nums[i]
                    i = (i-1)//2  
                else:
                    break
        elif val > self.nums[0]:
            self.nums[0] = val
            i = 0
            while 2 * i + 1 < len(self.nums):
                if 2 * i + 2 < len(self.nums):
                    if self.nums[i] > self.nums[2*i+1]:
                        if self.nums[2*i+1] <= self.nums[2*i+2]:
                            self.nums[i], self.nums[2*i+1] = self.nums[2*i+1], self.nums[i]
                            i = 2 * i + 1
                        else:
                            self.nums[i], self.nums[2*i+2] = self.nums[2*i+2], self.nums[i]
                            i = 2 * i + 2
                    elif self.nums[i] > self.nums[2*i+2]:
                        self.nums[i], self.nums[2*i+2] = self.nums[2*i+2], self.nums[i]
                        i = 2 * i + 2
                    else:
                        break
                else:
                    if self.nums[i] > self.nums[2*i+1]:
                        self.nums[i], self.nums[2*i+1] = self.nums[2*i+1], self.nums[i]
                        i = 2 * i + 1
                    else:
                        break
        
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
