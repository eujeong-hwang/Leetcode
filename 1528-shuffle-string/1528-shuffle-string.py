class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        listofs = []
        totalDict = {}
        shuffle = ""
        
        for i in range(len(s)):
            listofs.append(s[i])
        
        for i in range(len(indices)):
            totalDict[indices[i]] = listofs[i]
        
        for i in range(len(totalDict)):
            shuffle += totalDict[i]
            
        return shuffle