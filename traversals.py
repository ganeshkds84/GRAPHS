from collections import deque

class Solution:
    
    def bfsOfGraph(self,V,edges):
        
        graph=[[] for _ in range(V)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited=[False]*V
        result=[]
        q=deque()
        q.append(0)
        visited[0]=True
        while q:
            # print(q)
            node=q.popleft()
            result.append(node)
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    q.append(neighbour)
        return result
        
    def dfsOfGraph(self,V,edges):
        
        graph=[[] for _ in range(V)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited=[False]*V
        result=[]
        
        def dfs(node):
            visited[node]=True
            result.append(node)
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            
        dfs(0)
        return result
        
if __name__=='__main__':
    
    answer=Solution()
    print(answer.bfsOfGraph(5,[ [0, 1], [0, 2], [0, 3], [2, 4] ]))
    print(answer.dfsOfGraph(5,[ [0, 1], [0, 2], [0, 3], [2, 4] ]))