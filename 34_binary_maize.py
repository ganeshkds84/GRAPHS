from collections import deque
class Solution:
    def findPath(self,grid,source,destination):
        rows=len(grid)
        cols=len(grid[0])
        distance=[[float('inf') for _ in range(cols)] for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j]==1:
        #             distance[i][j]=1
        distance[source[0]][source[1]]=0
        q=deque()
        q.append(source)
        directions=[
            (0,-1),
            (-1,0),
            (1,0),
            (0,1)
        ]
        while q:
            r,c=q.popleft()
            # print(q)
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    # print('entered')
                    temp=distance[r][c]+1
                    if temp<distance[nr][nc]:
                        distance[nr][nc]=temp
                        q.append((nr,nc))
        if distance[destination[0]][destination[1]]==float('inf'):
            return -1
                    
        return distance[destination[0]][destination[1]]
    
if __name__=='__main__':
    grid = [[1, 0, 1],[1, 1, 0],[1, 1, 1]]
    source = [0, 0]
    destination = [2, 2]
    Ashu=Solution()
    print(Ashu.findPath(grid,source,destination))
    