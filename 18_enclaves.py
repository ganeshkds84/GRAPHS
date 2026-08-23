from collections import deque
class Solution:
    def numEnclaves(self,grid):
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        for i in range(cols):
            if grid[0][i]==1:
                q.append((0,i))
                grid[0][i]='safe'
            if grid[rows-1][i]==1:
                q.append((rows-1,i))
                grid[rows-1][i]='safe'
        for j in range(1,rows-1):
            if grid[j][0]==1:
                grid[j][0]='safe'
                q.append((j,0))
            if grid[j][cols-1]==1:
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
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]='safe'
                    q.append((nr,nc))
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count+=1
        return count
    
if __name__=='__main__':
    grid=[[0, 0, 0, 1],[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    Ashu=Solution()
    print(Ashu.numEnclaves(grid))