class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0 
        r = mountainArr.length() - 1

        pivot = 0

        while l <= r:
            m = l + (r - l) // 2

            leftVal = mountainArr.get(m - 1) if m - 1 >= 0 else float("-infinity")
            rightVal = mountainArr.get(m + 1) if m + 1 < mountainArr.length() else float("-infinity")
            middleVal = mountainArr.get(m)

            if middleVal > rightVal and middleVal > leftVal:
                pivot = m
                break

            elif middleVal < rightVal:
                l = m + 1
            else:
                r = m - 1

        
        l = 0
        r = pivot

        while l <= r:
            m = l + (r - l) // 2

            if mountainArr.get(m) > target:
                r = m - 1
            elif mountainArr.get(m) < target:
                l = m + 1
            else:
                return m


        l = pivot + 1
        r = mountainArr.length() - 1

        while l <= r:
            m = l + (r - l) // 2

            if mountainArr.get(m) > target:
                l = m + 1
            elif mountainArr.get(m) < target:
                r = m - 1
            else:
                return m
        
        return - 1     