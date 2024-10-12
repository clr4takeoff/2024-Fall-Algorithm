#SCC_Example

from collections import defaultdict

# Graph 클래스: 방향 그래프를 표현하는 클래스
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # 인접 리스트 (adjacency list)
        self.V = vertices  # 정점의 수 (number of vertices)

    # 간선을 그래프에 추가하는 함수
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # 첫 번째 단계에서 사용하는 DFS 유틸리티 함수 (역방향 그래프 G^R에서 실행)
    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    # 그래프의 전치(transpose) 그래프를 얻는 함수 (간선을 뒤집은 그래프 생성)
    def get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # 원래 그래프에서 DFS를 수행하는 유틸리티 함수
    def dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited, component)

    # Kosaraju 알고리즘을 사용해 SCC(강하게 연결된 컴포넌트)를 찾는 함수
    def kosaraju_scc(self):
        stack = []
        visited = [False] * self.V

        # 1단계: 역방향 그래프 G^R에서 DFS를 수행해 postvisit 순서대로 스택에 쌓기
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # 2단계: 전치된 그래프 (G^R)을 얻음
        gr = self.get_transpose()

        # 3단계: 모든 정점을 방문하지 않은 상태로 초기화 (두 번째 DFS를 위해)
        visited = [False] * self.V

        # 4단계: 스택에 쌓인 순서대로 원래 그래프에서 DFS 수행
        sccs = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gr.dfs_util(i, visited, component)
                sccs.append(component)

        return sccs

# 문자열 정점(A, B, C...)을 정수로 매핑하는 헬퍼 함수
def map_vertices(edges):
    mapping = {}
    reverse_mapping = {}
    current_index = 0

    # 문자열 정점을 정수로 매핑
    for u, v in edges:
        if u not in mapping:
            mapping[u] = current_index
            reverse_mapping[current_index] = u
            current_index += 1
        if v not in mapping:
            mapping[v] = current_index
            reverse_mapping[current_index] = v
            current_index += 1

    # 매핑된 정점들로 간선을 변환
    mapped_edges = [(mapping[u], mapping[v]) for u, v in edges]

    return mapped_edges, reverse_mapping

# 주어진 엣지들 (문자열로 표현된 정점들)
edges = [
    ('A', 'D'),
    ('B', 'A'), ('B', 'F'),
    ('C', 'A'),
    ('D', 'C'),
    ('E', 'B'),
    ('F', 'E'), ('F', 'A'),
    ('G', 'E'), ('G', 'F'), ('G', 'H'),
    ('H', 'E'), ('H', 'G')
]

# 문자열 정점들을 정수로 매핑
mapped_edges, reverse_mapping = map_vertices(edges)

# 정점의 수에 맞게 그래프 생성
g = Graph(len(reverse_mapping))

# 매핑된 간선을 그래프에 추가
for u, v in mapped_edges:
    g.add_edge(u, v)

# Kosaraju 알고리즘 실행하여 SCC 찾기
sccs = g.kosaraju_scc()

# 결과를 다시 문자열 정점으로 변환
sccs_with_labels = [[reverse_mapping[v] for v in scc] for scc in sccs]

# SCC 결과 출력
sccs_with_labels
