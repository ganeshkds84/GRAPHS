from collections import deque
class Solution:
    def cheapestFlight(self,n,flights,src,dst,k):
        graph=[[] for _ in range(n)]
        for u,v,cost in flights:
            graph[u].append((v,cost))
        distance=[float('inf') for _ in range(n)]
        distance[src]=0
        q=deque()
        q.append((0,src))
        count=k
        while q:
            for i in range(len(q)):
                current_cost,node=q.popleft()
                print(distance)
                if count==-1:
                    return distance[dst]
                for neighbour,cost in graph[node]:
                    new_cost=current_cost+cost
                    if new_cost<distance[neighbour]:
                        distance[neighbour]=new_cost
                        q.append((new_cost,neighbour))
            count-=1
        if distance[dst]==float('inf'):
            return -1
        else:
            return distance[dst]
if __name__=='__main__':
    n = 10
    flights=[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
    src = 6
    dst = 0
    k = 7
    Ashu=Solution()
    print(Ashu.cheapestFlight(n,flights,src,dst,k))