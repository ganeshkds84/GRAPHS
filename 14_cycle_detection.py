from collections import deque
class Solution:
    def cycleDetection(self,V,adj):
        visited=[False]*V
        for start in range(V):
            if visited[start]:
                continue
            q=deque()
            q.append((start,-1))
            visited[start]=True
            while q:
                node,parent=q.popleft()
                
                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        visited[neighbour]=True
                        q.append((neighbour,node))
                    elif neighbour!=parent:
                        return True
        return False
        
        
if __name__=='__main__':
    adj= [[1, 2], [0], [0, 3], [2]]
    V=4
    Ashu=Solution()
    print(Ashu.cycleDetection(V,adj))
        