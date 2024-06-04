from collections import defaultdict

def solution(edges):
    answer = [0] * 4
    
    def dfs(start):
        stack = [(start)]
        v = set()
        mode = 0
        cnt = defaultdict(int)
        while stack:
            spot = stack.pop()
            
            if len(graph[spot]) > 1:
                return 3
            
            for node in graph[spot]:
                if node == start:
                    return 1
    
                v.add(node)
                stack.append(node)
        
        return 2
        
    
    # 그래프 세팅
    graph = defaultdict(list)    
    for a, b in edges:
        graph[a].append(b)
    
    visited = set()
    nodes = set()
    
    for node, posts in graph.items():
        visited.update(posts)
        nodes.add(node)
        
    addi_node = tuple(nodes - visited)
    
    
    for n in addi_node:
        if len(graph[n]) > 1:
            target = n
    
    answer[0] = target
    
    
    for start in graph[target]:
        answer[dfs(start)] += 1
        
    
    return answer