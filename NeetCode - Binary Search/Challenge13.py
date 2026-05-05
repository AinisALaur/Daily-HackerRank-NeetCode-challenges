class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A = nums1
        B = nums2

        if len(B) < len(A):
            A, B = B, A

        size = len(A) + len(B)
        half = size // 2

        l = 0
        r = len(A) - 1

        while True:
            i = l + (r - l) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            print(Aleft, Aright, Bleft, Bright)

            if Aleft <= Bright and Aright >= Bleft:
                if size % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

A = [4, 5, 7]
B = [1, 2, 3, 6]
sol = Solution()
print(sol.findMedianSortedArrays(A, B))