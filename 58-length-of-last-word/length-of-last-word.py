class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        n=len(words)
        word=words[n-1]

        return len(word)