from collections import deque
class Solution:
    def shortestPath(self,n,m,edges):
        #create a graph
        graph=[[] for _ in range(n)]
        #indegree
        indegree=[0]*n
        #creating a queue
        q=deque()
        #Assigning distances to be infinity
        distance=[float('inf') for _ in range(n)]
        for u,v,weight in edges:
            graph[u].append((v,weight))
            indegree[v]+=1
        #topological sort order
        topo=[]
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            topo.append(node)
            for neighbour,weight in graph[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        #Relaxing the nodes in topo order
        distance[0]=0
        for node in range(n):
            if distance[node]==float('inf'):
                continue
            for neighbour,weight in graph[node]:
                temp=distance[node]+weight
                if temp<distance[neighbour]:
                    distance[neighbour]=temp
                    
        #Unreachable nodes
        for i in range(n):
            if distance[i]==float('inf'):
                distance[i]=-1
                
        return graph,indegree,topo,distance
    
if __name__=='__main__':
    n=int(input("Enter number of vertices:"))
    m=int(input('Enter number of edges:'))
    edges= [[0,1,2],[0,2,1],[3,4,2]]
    Ashu=Solution()
    print(Ashu.shortestPath(n,m,edges))