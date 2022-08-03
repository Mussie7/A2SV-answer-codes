class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = dict(Counter(nums))
        freq_list = []
        for num, freq in freq_dic.items():
            heapq.heappush(freq_list, [freq, num])
            if len(freq_list) > k:
                heapq.heappop(freq_list)

        return [heapq.heappop(freq_list)[1] for i in range(len(freq_list))]
