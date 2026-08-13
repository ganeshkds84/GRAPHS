class Solution:
    
    def FindProvinces(self,adj):
        
        n=len(adj)
        visited=[False]*n
        provinces=0
        
        def dfs(node):
            visited[node]=True
            
            for neighbour in range(n):
                if adj[node][neighbour]==1 and not visited[neighbour]:
                    dfs(neighbour)
                    
        for i in range(n):
            if not visited[i]:
                provinces+=1
                dfs(i)
        return provinces

if __name__=='__main__':
    adj= [ [1, 1], [1, 1] ]
    answer=Solution()
    print(answer.FindProvinces(adj))