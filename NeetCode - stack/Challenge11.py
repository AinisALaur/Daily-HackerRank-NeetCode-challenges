class Solution:
    def simplifyPath(self, path: str) -> str:
        pathParts = []
        currPath = ""
        for char in path + "/":
            if char == '/':
                if currPath == "..":
                    if len(pathParts) > 0:
                        pathParts.pop()

                elif currPath != "." and len(currPath) > 0:
                    pathParts.append(currPath)
                
                currPath = ""

            else:
                currPath += char
        
        return "/" + "/".join(pathParts)
    
sol = Solution()
print(sol.simpliftPath("/neetcode/practice//...///../courses"))