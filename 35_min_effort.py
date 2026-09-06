import heapq
class Solution:
    def minEffort(self,heights):
        rows=len(heights)
        cols=len(heights[0])
        pq=[]
        heapq.heappush(pq,(0,(0,0)))
        directions=[
            (0,-1),(-1,0),(1,0),(0,1)
        ]    
        effort=[[(10**9) for _ in range(cols)] for _ in range(rows)]
        effort[0][0]=0
        while pq:
            current_effort,(r,c)=heapq.heappop(pq)
            # print(r,c)
            print(effort)
            if current_effort>effort[r][c]:
                continue            
            if r==rows-1 and c==cols-1:
                return current_effort
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    diff=abs(heights[nr][nc]-heights[r][c])
                    new_effort=max(current_effort,diff)
                    if new_effort<effort[nr][nc]:
                        effort[nr][nc]=new_effort
                        heapq.heappush(pq,(new_effort,(nr,nc)))
            
        return -1

if __name__=='__main__':
    grid= [[1,2,2],[3,8,2],[5,3,5]]
    Ashu=Solution()
    print(Ashu.minEffort(grid))