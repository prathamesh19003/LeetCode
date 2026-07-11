class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        for i in range(len(s)):
            if s[i]==')':
                count-=1
            if count>0:
                res.append(s[i])
            if s[i]=='(':
                count+=1
        return ''.join(res)
            