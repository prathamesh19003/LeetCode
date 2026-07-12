class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            res=self.checkPalindrome(words[i])
            if res is True:
                return words[i]
        return ""
    def checkPalindrome(self,s:str)->bool:
        reversed_string=s[::-1]

        if reversed_string==s:
            return True
        return False