"""
n = 2

()()
(())


"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def dfs (text, opening, closing):
            
            if opening ==n and closing == n : 
                return answer.append(text)
            
            if opening > n or opening < closing :
                return 

            dfs(text + "(", opening + 1, closing )
            dfs(text + ")", opening, closing + 1)
            
        dfs("", 0, 0)
        return answer


