import heapq
class Solution:
    def destinationWays(self,n,roads):
        graph=[[] for _ in range(n)]
        for u,v,cost in roads:
            graph[u].append((cost,v))
            graph[v].append((cost,u))
        pq=[]
        heapq.heappush(pq,(0,0))
        distance=[float('inf') for _ in range(n)]
        distance[0]=0
        ways=[0 for _ in range(n)]
        ways[0]=1
        while pq:
            current_cost,node=heapq.heappop(pq)
            if current_cost>distance[node]:
                continue
            for cost,neighbour in graph[node]:
                new_cost=current_cost+cost
                if new_cost<distance[neighbour]:
                    distance[neighbour]=new_cost
                    ways[neighbour]=ways[node]
                    heapq.heappush(pq,(new_cost,neighbour))
                elif new_cost==distance[neighbour]:
                    ways[neighbour]+=ways[node]
        return ways[n-1]

if __name__=='__main__':
    routes=  [[0,1,1],[0,2,1],[0,3,1],[1,3,1],[2,3,1]]
    n=4
    m=5
    Ashu=Solution()
    print(Ashu.destinationWays(n,routes))