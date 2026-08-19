from collections import deque
class Solution:
    def scheduleCourses(self,numCourses,prerequisites):
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        
        for course,prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course]+=1
            
        q=deque()
        print(indegree)
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                print(f"{i,q}")
        count=0
        
        while q:
            node=q.popleft()
            count+=1
            print(q)
            print(indegree)
            
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                
                if indegree[neighbour]==0:
                    q.append(neighbour)
                    
        return count==numCourses
    
if __name__=='__main__':
    numCourses=2
    preReq=[[1,0],[0,1]]
    Ashu=Solution()
    print(Ashu.scheduleCourses(numCourses,preReq))