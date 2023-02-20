class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(x) for x in str(n)]
        
        productOfDigits = 1
        sumOfDigits = 0
        
        for i in range(len(res)):
            productOfDigits *= res[i]
        
        for i in range(len(res)):
            sumOfDigits += res[i]
        
        diff = productOfDigits - sumOfDigits
        return diff