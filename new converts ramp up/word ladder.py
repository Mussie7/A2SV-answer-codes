class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque([beginWord])
        count = 0
        
        if endWord not in wordList:
            return 0
        
        if len(beginWord) == 1:
            return 2
        
        while q:
            count += 1
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return count
                
                temp = set()
                for wrd in wordList:
                    if word[0] != wrd[0] and word[-1] != wrd[-1]:
                        continue
                        
                    cnt = 0
                    for i in range(len(word)):
                        if word[i] != wrd[i]:
                            cnt += 1

                        if cnt > 1:
                            break

                        if i == len(word) - 1:
                            q.append(wrd)
                            temp.add(wrd)

                for wd in temp:
                    if wd in wordList:
                        wordList.remove(wd)

        return 0
