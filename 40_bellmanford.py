import heapq
class Solution:
    def bellmanFord(self,V,edges,source):
        distance=[10**9 for _ in range(V)]
        distance[source]=0
        # print(distance)
        for i in range(V-1):
            for u,v,weight in edges:
                if distance[u]==10**9:
                    continue
                if distance[u]+weight<distance[v]:
                    distance[v]=distance[u]+weight
            # print(distance)
        for u,v,weight in edges:
            if distance[u]+weight<distance[v]:
                return [-1]
        return distance
    
if __name__=='__main__':
    edges=[[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]
    n=6
    s=0
    Ashu=Solution()
    print(Ashu.bellmanFord(n,edges,s))