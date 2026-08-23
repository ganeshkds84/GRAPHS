from collections import deque
class Solution:
    def findSurrouned(self,grid):
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        for i in range(cols):
            if grid[0][i]=="O":
                grid[0][i]='safe'
                q.append((0,i))
            if grid[rows-1][i]=="O":
                grid[rows-1][i]='safe'
                q.append((rows-1,i))
        for j in range(1,rows-1):
            if grid[j][0]=="O":
                grid[j][0]='safe'
                q.append((j,0))
            if grid[j][cols-1]=="O":
                grid[j][cols-1]='safe'
                q.append((j,cols-1))
        directions=[
            (-1,0),
            (0,-1),
            (0,1),
            (1,0)
        ]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="O":
                    grid[nr][nc]='safe'
                    q.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='safe':
                    grid[i][j]="O"
                else:
                    grid[i][j]="X"
        return grid
    
if __name__=='__main__':
    grid= [ ["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"] ]
    Ashu=Solution()
    print(Ashu.findSurrouned(grid))
    