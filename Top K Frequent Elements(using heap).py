class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        freq_list = []
        for num, freq in dic.items():
            freq_list.append([freq, num])
        
        heapq.heapify(freq_list)

        return [i[1] for i in heapq.nlargest(k, freq_list)]
