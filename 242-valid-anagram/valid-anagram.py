class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        new1=''.join(sorted(s))
        new2=''.join(sorted(t))

        if new1==new2:
            return True
        return False