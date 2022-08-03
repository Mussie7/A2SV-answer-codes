class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = dict(Counter(words))
        
        freq_dic = {}
        for word in dic:
            if dic[word] in freq_dic:
                freq_dic[dic[word]].append(word)
            else:
                freq_dic[dic[word]] = [word]
        
        freq_list = []
        for freq, word in freq_dic.items():
            heapq.heappush(freq_list, [freq, word])
            if len(freq_list) > k:
                heapq.heappop(freq_list)

                
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
