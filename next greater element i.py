class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        stack.append(nums2.pop(0))
        while nums2:
            if nums2[0] < stack[-1]:
                stack.append(nums2.pop(0))
            else:
                while stack and nums2[0] > stack[-1]:
                    next_greater[stack.pop()] = nums2[0]
                stack.append(nums2.pop(0))
        while stack:
            next_greater[stack.pop()] = -1
        result = []
        for i in nums1:
            result.append(next_greater[i])
        return result
