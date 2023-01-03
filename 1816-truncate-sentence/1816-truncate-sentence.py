class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        sentence = " "
        x = s.split(" ")
        
        for i in range(k):
            if i == 0:
                sentence = x[i]
            else:
                sentence += " " + x[i]
            
        return sentence
            