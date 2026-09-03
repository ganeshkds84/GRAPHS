import heapq
class Solution:
    def shortestPath(self,N,edges,S):
        #creating a graph
        graph=[[] for _ in range(N)]
        for u,v,weight in edges:
            graph[u].append((weight,v))
            graph[v].append((weight,u))
        #calculate distance
        distance=[10**9]*N
        distance[S]=0
        pq=[]
        heapq.heappush(pq,(0,S))
        while pq:
            # print(pq)
            # print(distance)
            current_distance,node=heapq.heappop(pq)
            if current_distance>distance[node]:
                continue
            for weight,neighbour in graph[node]:
                temp=current_distance+weight
                if temp<distance[neighbour]:
                    distance[neighbour]=temp
                    heapq.heappush(pq,(temp,neighbour))
        
        return distance
    
if __name__=='__main__':
    n=int(input("Enter total number of vertices:"))
    edges=[[0,1,1],[0,3,2],[1,2,4],[2,3,3]]
    s=int(input("Enter the source vertex:"))
    Ashu=Solution()
    print(Ashu.shortestPath(n,edges,s))