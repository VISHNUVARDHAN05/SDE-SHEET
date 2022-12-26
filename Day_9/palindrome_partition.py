class Solution:
    def partition(self, s: str):
        self.answer = []
        self.find(s, 0, [], 0)
        return self.answer

    def find(self, s, i, ps, l):
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                psCopy = list(ps)
                psCopy.append(s[i:j + 1])
                self.find(s, j + 1, psCopy, l + j - i + 1)

        if l == len(s):
            self.answer.append(ps)

    def isPalindrome(self, s, i, j):
        l = i
        r = j
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
x=Solution()
print(x.partition("aabb"))