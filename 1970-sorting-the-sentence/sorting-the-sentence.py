class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        ans = [""] * len(words)
        
        for word in words:
            index = int(word[-1]) - 1 
            ans[index] = word[:-1]
            
        return " ".join(ans)
