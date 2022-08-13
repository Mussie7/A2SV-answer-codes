class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_dic = {}
        for edge in edges:
            if edge[0] in edge_dic:
                edge_dic[edge[0]].add(edge[1])
            else:
                edge_dic[edge[0]] = {edge[1]}
            
            if edge[1] in edge_dic:
                edge_dic[edge[1]].add(edge[0])
            else:
                edge_dic[edge[1]] = {edge[0]}
        
        # a solution that results in a TLE exception
        # def dfs(node, edge_dic, dist):
        #     nonlocal visited, count
            
            # temp = edge_dic[node] - visited
            # visited = visited.union(temp)
            # count += len(temp) * dist
            
            # for nodes in temp:
            #     dfs(nodes, edge_dic, dist + 1)
            
        # # print(edge_dic)
        # ans = [0] * n
        # if n == 1:
        #     return ans
        
        # for i in range(n):
        #     visited = {i}
        #     count = 0
        #     dfs(i, edge_dic, 1)
        #     ans[i] = count
        
        # return ans
        
        ans, count = [0] * n, [1] * n
        def stsum(node, edge_dic, parent = None):
            for edge in edge_dic[node]:
                if edge != parent:
                    stsum(edge, edge_dic, node)
                    count[node] += count[edge]
                    ans[node] += ans[edge] + count[edge]
        
        def dfs(node, edge_dic, parent = None):
            for edge in edge_dic[node]:
                if edge != parent:
                    ans[edge] = ans[node] + (n - count[edge]) -  count[edge]
                    dfs(edge, edge_dic, node)
        
        if n == 1:
            return ans
        
        stsum(0, edge_dic)
        dfs(0, edge_dic)
        
        return ans
