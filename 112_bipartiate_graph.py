from collections import deque
class Solution:
    def isBipartiate(self,V,edges):
        graph=[[] for _ in range(V)]
        for u,v in edges:
            # print(u,v)
            graph[u].append(v)
            graph[v].append(u)
        color=[-1]*V
        q=deque()
        for start in range(V):
            if color[start]!=-1:
                continue
            q.append(start)
            color[start]=0
            while q:
                node=q.popleft()
                for neighbour in graph[node]:
                    if color[neighbour]==-1:
                        if color[node]==0:
                            color[neighbour]=1
                            q.append(neighbour)
                        else:
                            color[neighbour]=0
                            q.append(neighbour)
                    elif color[node]==color[neighbour]:
                        return False             
        return True
    
if __name__=='__main__':
    edges=  [ [0, 1], [0, 2], [0, 3], [2, 1], [3, 2] ]
    V=4
    Ashu=Solution()
    print(Ashu.isBipartiate(V,edges))