class Solution:

    def encode(self, strs: List[str]) -> str:
        m =""
        for n in strs :
            m = m+n+"❓"
        return m 
        
    def decode(self, s: str) -> List[str]:
        s_list = s.split("❓")
        return s_list[:-1]
