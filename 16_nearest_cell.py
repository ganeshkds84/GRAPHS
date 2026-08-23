from collections import deque
class Solution:
    def findNearest(self,grid):
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        final=[[ float('inf') for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    final[i][j]=0
                    q.append((i,j))
        directions=[
            (-1,0),
            (0,-1),
            (1,0),
            (0,1)
        ]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and final[nr][nc]==float('inf'):
                    final[nr][nc]=final[r][c]+1
                    q.append((nr,nc))
                
        return final
    
if __name__=='__main__':
    grid= [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1] ]
    Ashu=Solution()
    print(Ashu.findNearest(grid))

