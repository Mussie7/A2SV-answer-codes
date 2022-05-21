class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        scores = [0] * len(questions)
        max_score = 0
        max_dic = {}
        for i in reversed(range(len(questions))):
            scores[i] += questions[i][0]

            if questions[i][1] < len(questions) - i - 1:
                scores[i] += max_dic[i+questions[i][1]+1]
            
            if i + 1 in max_dic.keys():
                max_dic[i] = max(max_dic[i+1], scores[i])
            else:
                max_dic[i] = max(scores)
            max_score = max(scores[i], max_score)
        
        return max_score
