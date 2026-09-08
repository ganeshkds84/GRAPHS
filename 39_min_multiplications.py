from collections import deque
class Solution:
    def minMulti(self,arr,start,end):
        MOD=10**5
        q=deque()
        q.append(start)
        count=1
        visited=[False for _ in range(MOD)]
        visited[start]=True
        while q:
            print(count)
            for i in range(len(q)):
                start=q.popleft()
                # print(node)
                for j in range(len(arr)):
                    new_start=(start*arr[j])%MOD
                    # print(req)
                    if new_start==end:
                        return count
                    if not visited[new_start]:
                        visited[new_start]=True
                        q.append(new_start)
            count+=1

if __name__=='__main__':
    arr=[3,4,65]
    s=7
    e=21
    Ashu=Solution()
    print(Ashu.minMulti(arr,s,e))