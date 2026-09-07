from collections import deque
class Solution:
    def networkDelay(self,times,n,k):
        graph=[[] for _ in range(n)]
        for u,v,time in times:
            graph[u-1].append((time,v-1))
        q=deque()
        q.append((0,k-1))
        distance=[float('inf')]*n
        distance[k-1]=0
        while q:
            current_time,node=q.popleft()
            for time,neighbour in graph[node]:
                new_time=current_time+time
                if new_time<distance[neighbour]:
                    distance[neighbour]=new_time
                    q.append((new_time,neighbour))
                
        return -1 if max(distance)==float('inf') else max(distance)
    
if __name__=='__main__':
    times=[[2,1,1],[2,3,1],[3,4,1]]
    n=4
    k=2
    Ashu=Solution()
    print(Ashu.networkDelay(times,n,k))