# Chap4_25p_Example of Kruskal’s algorithm using Union-find

class DisjointSet:
    def __init__(self, n):
        # 부모 노드를 자기 자신으로 초기화
        self.parent = list(range(n))
        # 각 트리의 랭크 (높이) 초기화
        self.rank = [0] * n

    def find(self, u):
        # 경로 압축 기법 적용
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # 각 집합의 루트 노드 찾기
        root_u = self.find(u)
        root_v = self.find(v)
        
        # 두 집합을 합치기 (랭크를 고려하여 더 작은 트리를 큰 트리에 붙임)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    # vertices는 정점 리스트, edges는 (가중치, u, v) 형태의 튜플 리스트
    edges = sorted(edges, key=lambda edge: edge[0])  # 간선을 가중치에 따라 정렬
    n = len(vertices)  # 정점의 수
    dsu = DisjointSet(n)  # DisjointSet 초기화
    
    mst_edges = []  # 최소 신장 트리의 간선 집합
    mst_weight = 0  # 최소 신장 트리의 총 가중치
    
    for weight, u, v in edges:
        # 두 정점이 서로 다른 집합에 속해 있으면, 해당 간선을 MST에 추가
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst_edges.append((u, v, weight))  # 간선 추가
            mst_weight += weight
    
    return mst_edges, mst_weight

# 주어진 그래프의 정점과 간선
vertices = [0, 1, 2, 3, 4]  # 정점 리스트
edges = [
    (3, 0, 3),  # (가중치, 정점 u, 정점 v)
    (12, 0, 4),
    (7, 2, 4),
    (2, 1, 2),
    (3, 3, 2),
    (5, 1, 3)
]

# Kruskal's 알고리즘 실행
mst_edges, total_weight = kruskal(vertices, edges)

# 결과 출력
print("Minimum Spanning Tree (MST)의 간선들:", mst_edges)
print("MST의 총 가중치:", total_weight)
