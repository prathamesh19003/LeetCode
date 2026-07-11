class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        visited=set()

        while n not in visited:
            visited.add(n)
            n=self.squareOfNumber(n)

            if n==1:
                return True
        return False
    
    def squareOfNumber(self,n:int)->int:
        squared_number=0
        while n:
            num=n%10
            squared_number+=num**2
            n=n//10
        return squared_number