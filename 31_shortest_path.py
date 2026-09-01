from collections import deque
class Solution:
    def shortPath(self,n,m,edges):
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distance=[-1]*n
        print(distance)
        q=deque()
        for start in range(n):
            if distance[start]==-1:
                q.append(start)
                distance[start]=0
            while q:
                node=q.popleft()
                print(distance)
                for neighbour in graph[node]:
                    if distance[neighbour]==-1:
                        q.append(neighbour)
                        distance[neighbour]=distance[node]+1
                    
        return distance

if __name__=='__main__':
    n=int(input("Enter number of vertices:"))
    m=int(input("Enter number of edges:"))
    edges= [[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]
    Ashu=Solution()
    print(Ashu.shortPath(n,m,edges))