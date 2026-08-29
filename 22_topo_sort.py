class Solution:
    def topoSort(self,n,edges):
        graph=[[] for _ in range(n)]
        # indegree=[0]*n 
        for u,v in edges:
            graph[u].append(v)
            # indegree[v]+=1
        result=[]
        visited=[False]*n
        def dfs(node):
            visited[node]=True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            result.append(node)
        for start in range(n):
            if not visited[start]:
                dfs(start)
        result.reverse()    
        return result
    
if __name__=='__main__':
    v=int(input("Enter number of vertices:"))
    edges=[[5,0],[5,2],[4,0],[4,1],[3,1],[2,3]]
    Ashu=Solution()
    print(Ashu.topoSort(v,edges))