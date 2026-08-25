from collections import deque
class Solution:
    def numIslands(self,grid):
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        islands=0
        directions=[
            (-1,0),(0,-1),(1,0),(0,1),
            (1,1),(-1,1),(1,-1),(-1,-1)
        ]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and visited[i][j]==False:
                    visited[i][j]=True
                    q.append((i,j))
                    islands+=1
                while q:
                    r,c=q.popleft()
                    for dr,dc in directions:
                        nr=r+dr
                        nc=c+dc
                        if 0<=nr<rows and 0<=nc<cols and visited[nr][nc]==False and grid[nr][nc]=='1':
                            visited[nr][nc]=True
                            q.append((nr,nc))
            # islands+=1
        return islands
    
if __name__=='__main__':
    Ashu=Solution()
    grid=[ ["1", "1", "1", "0", "1"], ["1", "0", "0", "0", "0"], ["1", "1", "1", "0", "1"], ["0", "0", "0", "1", "1"] ]
    print(Ashu.numIslands(grid))
    