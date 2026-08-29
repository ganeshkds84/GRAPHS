from collections import deque
class Solution:
    def detectCycle(self,V,graph):
        visited=[False]*V
        pathVisited=[False]*V
        def dfs(node):
            visited[node]=True
            pathVisited[node]=True
            # print(pathVisited)
            for neighbour in graph[node]:
                # print(neighbour)
                if visited[neighbour]==False:
                    if dfs(neighbour):
                        return True
                elif pathVisited[neighbour]:
                    # print('entered')
                    return True
                # print(pathVisited)
                
            pathVisited[node]=False
            return False

        for start in range(V):
            if not visited[start]:
                if dfs(start):
                    return True
                
        return False
if __name__=='__main__':
    adj= [ [], [0, 2, 5], [3], [4], [1], [ ] ]
    n=6
    Ashu=Solution()
    print(Ashu.detectCycle(n,adj))