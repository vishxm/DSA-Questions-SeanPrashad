class Solution:
    def countBits(self, n: int) -> List[int]:
        resArray = [0]*(n+1)
        for i in range(1,n+1):
            resArray[i] = resArray[int(i//2)] + i%2

        return resArray