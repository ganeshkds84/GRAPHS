class Solution:
    def floydWarshall(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        #convert unreachable edges to infinity distance
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==-1:
                    matrix[i][j]=float('inf')
        #Use via to travel from start node to end node
        for via in range(rows):
            for start in range(rows):
                for end in range(rows):
                    if start ==end:
                        continue
                    temp=matrix[start][via]+matrix[via][end]
                    # print(start,via,end,temp)
                    if temp<matrix[start][end]:
                        matrix[start][end]=temp
                            
        return matrix
    
if __name__=='__main__':
    mat=[[0, 2, -1, -1],[1, 0, 3, -1],[-1, -1, 0, 1],[3, 5, 4, 0]]
    Ashu=Solution()
    print(Ashu.floydWarshall(mat))