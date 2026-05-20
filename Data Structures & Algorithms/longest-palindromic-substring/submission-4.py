class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer=s[:1]
        
        for n in range(len(s)):
            for m in range(n+1, len(s)+1):
                if s[n:m] == s[n:m][::-1] and len(answer) < len(s[n:m]) :
                    answer = s[n:m]
        return answer