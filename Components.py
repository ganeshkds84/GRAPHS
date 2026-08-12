class Solution:
    def FindComponents(self, V,edges):
        
        graph=[[] for _ in range(V)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited=[False]*V
        components=0
        
        def dfs(node):
            visited[node]=True
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
        
        for i in range(V):
            if not visited[i]:
                components+=1
                dfs(i)
        
        return components
    
if __name__=='__main__':
    
    answer=Solution()
    print(answer.FindComponents(5,[[0,1],[1,2]]))