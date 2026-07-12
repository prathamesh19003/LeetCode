class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            word=words[i]
            if word==word[::-1]:
                return word
        return ""