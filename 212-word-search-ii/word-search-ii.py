class Solution:
    def findWords(self, board, words):
        root = {}
        for w in words:
            node = root
            for char in w:
                node = node.setdefault(char, {})
            node['#'] = w
        
        rows, cols = len(board), len(board[0])
        res = []
        
        def dfs(r, c, parent):
            char = board[r][c]
            node = parent[char]
            word_found = node.pop('#', None)
            if word_found:
                res.append(word_found)
            
            board[r][c] = '#'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node:
                    dfs(nr, nc, node)
            board[r][c] = char
            
            if not node:
                parent.pop(char)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
        
        return res
