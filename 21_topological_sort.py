from collections import deque
class Solution:
    def topoSort(self,n,adj):
        indegree=[0]*n
        # edges=[]
        # for i in range(n):
        #     for j in range(len(adj[i])):
        #         edges.append([i,adj[i][j]])
        for u in range(n):
            for v in range(len(adj[u])):
                indegree[adj[u][v]]+=1
        q=deque()
        result=[]
        for start in range(n):
            if indegree[start]==0:
                q.append(start)
        while q:
            node=q.popleft()
            result.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        return result    
        
if __name__=="__main__":
    n=int(input("Enter number of vertices:"))
    graph=[ [ ], [ ], [3], [1], [0,1], [0,2] ]
    Ashu=Solution()
    print(Ashu.topoSort(n,graph))