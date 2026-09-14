import heapq
class Solution:
    def smallestNeighbours(self,n,m,edges,threshold):
        graph=[[] for _ in range(n)]
        for u,v,cost in edges:
            graph[u].append((v,cost))
            graph[v].append((u,cost))
        final=[0 for _ in range(n)]
        for start in range(n):
            distance=[float('inf') for _ in range(n)]
            pq=[]
            heapq.heappush(pq,(0,start))
            distance[start]=0
            while pq:
                current_cost,node=heapq.heappop(pq)
                for neighbour,cost in graph[node]:
                    new_cost=current_cost+cost
                    if new_cost<distance[neighbour]:
                        distance[neighbour]=new_cost
                        heapq.heappush(pq,(new_cost,neighbour))
            for i in range(n):
                if i==start:
                    continue
                if distance[i]<=threshold:
                    final[start]+=1
        required=float('inf')
        node=0
        for i in range(n):
            if final[i]<=required:
                required,node=final[i],i
        return node
    
if __name__=='__main__':
    N=3
    M=2
    edges = [[0,1,1],[0,2,3]]
    distanceThreshold = 2
    Ashu=Solution()
    print(Ashu.smallestNeighbours(N,M,edges,distanceThreshold))