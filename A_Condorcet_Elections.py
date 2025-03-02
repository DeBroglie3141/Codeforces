from collections import deque, defaultdict

n, m = map(int, input().split())
faits = [tuple(map(int, input().split())) for _ in range(m)]

def topological_sort(n, graph):
    in_degree = [0] * (n + 1)
    
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    ordre_topo = []
    while queue:
        node = queue.popleft()
        ordre_topo.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(ordre_topo) == n:
        return ordre_topo
    else:
        return None  # There's a cycle

def truc(n, m, faits):
    graphe = defaultdict(list)
    
    for a, b in faits:
        graphe[a].append(b)
    
    ordre_topo = topological_sort(n, graphe)
    
    if ordre_topo is None:
        print("NO")
        return
    
    print("YES")
    
    trucs_corrects = set(ordre_topo)

    k = len(trucs_corrects)
    for _ in range(k):
        print(" ".join(map(str, ordre_topo)))

truc(n, m, faits)


#Brooooooo WTF :(