from collections import deque
class Solution:
    def rottenOranges(self,grid):
        m=len(grid)
        n=len(grid[0])
        fresh=0
        rotten=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
                    
        directions=[
            (-1,0),
            (0,-1),
            (0,1),
            (1,0)
        ]
        minutes=0
        
        while rotten and fresh>0:
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        rotten.append((nr,nc))
                        fresh-=1
            minutes+=1
        # return grid
        if fresh==0:
            return minutes
        else:
            return -1
        
if __name__=='__main__':
    Ashu=Solution()
    grid =  [ [2,1,1] , [1,1,0] , [0,1,1] ] 
    print(Ashu.rottenOranges(grid))