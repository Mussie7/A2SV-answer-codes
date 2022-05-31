class Solution:
    def callable(self, n, right, left):
        # first count the number of zeros there is going to be in the final array
        def zeros(num):
            if num <= 1:
                return 0

            return (num % 2 == 0) + 2 * zeros(num//2)

        def recurse(num, start, end):
            # if it is out of bound no need to do the recursion
            if start > left or end < right:
                return 0

            # if it is inbound the number of ones is the same as the number inserted
            if start >= right and end <= left:
                return num

            mid = (start+end) // 2
            # finally return the sum of the recursions
            return recurse(num//2, start, mid-1) + recurse(num % 2, mid, mid) + recurse(num//2, mid+1, end)

        # since the number of ones in the final array are the same as the magnitude of the given number
        # e.g 7 = [1,1,1,1,1,1,1]
        # thus the whole size of the array is the sum of the number and the number of zeroes
        size = n + zeros(n)
        x = recurse(n, 1, size)

        return x


j = Solution()
t = input()
t = tuple(t.split())
print(j.callable(int(t[0]), int(t[1]), int(t[2])))
