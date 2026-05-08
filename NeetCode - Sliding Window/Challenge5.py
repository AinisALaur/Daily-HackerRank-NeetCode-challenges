class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        counts1 = {}

        for char in s1:
            if char not in counts1:
                counts1[char] = 1
            else:
                counts1[char] += 1

        def is_a_permutation():
            for key, val in counts1.items():
                if counts2.get(key, -1) != val:
                    return False
            
            return True

        counts2 = {}
        for j in range(len(s2)):
            if s2[j] not in counts2:
                counts2[s2[j]] = 1
            else:
                counts2[s2[j]] += 1

            if j - i + 1 == len(s1):
                if is_a_permutation():
                    return True
                else:
                    counts2[s2[i]] -= 1
                    i += 1

        return False
    
sol = Solution()
s1 = "abc"
s2 = "lecabee"
print(sol.checkInclusion(s1, s2))