from collections import deque
class Solution:
    def wordLadder(self,startWord,endWord,wordlist):
        q=deque()
        words=set(wordlist)
        if endWord not in words:
            return []
        q.append([startWord])
        # words.discard(startWord)
        result=[]
        while q:
            level_size=len(q)
            used_in_level=set()
            
            for _ in range(level_size):  
                paths=q.popleft()
                word=paths[-1]
                # print(word)
                if word==endWord:
                    result.append(paths)
                    continue
                                
                list_word=list(word)
                for i in range(len(list_word)):
                    original=list_word[i]
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        list_word[i]=ch
                        new=''.join(list_word)
                        if new in words:
                            new_path=paths+[new]
                            q.append(new_path)
                            used_in_level.add(new)
                            # print(q)
                    list_word[i]=original
            for task in used_in_level:
                words.discard(task)
        return result
    
if __name__=='__main__':
    startWord = "der"
    targetWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    Ashu=Solution()
    print(Ashu.wordLadder(startWord,targetWord,wordList))