from collections import deque
class Solution:
    def flood_fill(self,image,sr,sc,newColor):
        
        old=deque()
        m=len(image)
        n=len(image[0])
        
        directions=[
            (-1,0),
            (0,-1),
            (1,0),
            (0,1)
        ]
        
        old=deque()
        old.append((sr,sc))
        
        image[sr][sc]=newColor
        
        while old:
            for _ in range(len(old)):
                r,c=old.popleft()
                
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and image[nr][nc]==1:
                        image[nr][nc]=newColor                        
                        old.append((nr,nc))
                        # image[dr][dc]=newColour
                # print(image)
                
        return image
    
if __name__=='__main__':
    
    image=[ [1, 1, 1], [1, 1, 0], [1, 0, 1] ]
    sr,sc=1,1
    newColour=2
    Ashu=Solution()
    print(Ashu.flood_fill(image,sr,sc,newColour))
    