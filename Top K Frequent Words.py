class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        
        freq_dic = {}
        for word in dic:
            if dic[word] in freq_dic:
                freq_dic[dic[word]].append(word)
            else:
                freq_dic[dic[word]] = [word]
        
        freq_list = [list(i) for i in freq_dic.items()]      
        heapq.heapify(freq_list)
        highest = heapq.nlargest(k, freq_list)
        
        ans = []
        for i in range(len(highest)):
            highest[i][1].sort()
            ans.extend(highest[i][1])
            if len(ans) > k:
                while len(ans) > k:
                    ans.pop()
                break

        return ans
