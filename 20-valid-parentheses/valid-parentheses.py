class Solution(object):
    def isValid(self, s):
        stk = [0]
        mtch = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in mtch.values():
                stk.append(i)
            elif stk[-1] == mtch[i]:
                stk.pop()
            else:
                return False
        return not stk.pop()                