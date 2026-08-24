from collections import deque
class Solution:
    def wordLadder(self,wordlist,startWord,targetWord):
        q=deque()
        words=set(wordlist)
        if startWord not in words:
            return 0
        q.append((1,startWord))
        words.discard(startWord)
        while q:
            distance,word=q.popleft()
            # print(word)
            if word==targetWord:
                return distance
            new_word=list(word)
            for i in range(len(word)):
                original=new_word[i]
                for ch in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word[i]=ch
                    new="".join(new_word)
                    if new in words:
                        q.append((distance+1,new))
                        words.remove(new)
                new_word[i]=original
                        
        return 0
    
if __name__=='__main__':
    wordlist= ["des","der","dfr","dgt","dfs"]
    start='der'
    end='dfs'
    Ashu=Solution()
    print(Ashu.wordLadder(wordlist,start,end))