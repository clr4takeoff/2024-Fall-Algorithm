#chap4_Prim's Algorithm implementation using Priority Queue

import heapq

def prim(G, start):
    # 정점 이름 매핑 (숫자 -> 알파벳)
    vertex_names = ['A', 'B', 'C', 'D', 'E', 'F']

    # 초기화
    n = len(G)  # 정점의 수
    cost = [float('inf')] * n  # 각 정점의 최소 비용
    pre = [None] * n  # 이전 정점을 저장
    cost[start] = 0  # 시작 정점의 비용을 0으로 설정

    # 우선순위 큐 초기화 (cost 값을 기준으로)
    pq = [(0, start)]  # (cost, vertex)
    in_mst = [False] * n  # 정점이 MST에 포함되었는지 여부

    # MST가 완성될 때까지 계속 반복
    while pq:
        current_cost, u = heapq.heappop(pq)  # 현재 비용과 정점 선택
        if in_mst[u]:  # 이미 포함된 정점이면 무시
            continue

        in_mst[u] = True  # 현재 정점을 MST에 포함
        print(f"\n=== Step: Include vertex {vertex_names[u]} in MST with cost {current_cost} ===")

        # 선택할 수 있는 edge들 출력
        print(f"Current edges to choose from:")
        for v, weight in G[u]:
            if not in_mst[v]:
                print(f"  ({vertex_names[u]}, {vertex_names[v]}) with weight {weight}")

        # 인접한 정점들의 비용을 갱신
        for v, weight in G[u]:
            if not in_mst[v] and cost[v] > weight:
                print(f"  -> Update: cost({vertex_names[v]}) changes from {cost[v]} to {weight}, pre({vertex_names[v]}) = {vertex_names[u]}")
                cost[v] = weight  # 최소 비용 업데이트
                pre[v] = u  # 이전 정점 업데이트
                heapq.heappush(pq, (cost[v], v))  # 우선순위 큐에 갱신된 값 추가

    # MST 결과 출력
    print("\nFinal MST edges and their costs:")
    for i in range(n):
        if pre[i] is not None:
            print(f"Edge ({vertex_names[pre[i]]}, {vertex_names[i]}) with cost {cost[i]}")

# 그래프 인접 리스트 (무방향 그래프)
# (정점, 가중치)의 리스트로 표현
graph_list = [
    [(1, 4), (2, 1), (3, 3)],    # A (0)
    [(0, 4), (2, 4), (3, 4)],  # B (1)
    [(0, 1), (1, 4), (3, 2), (5, 4)],  # C (2)
    [(0, 3), (2, 2), (1, 4), (5, 6)],  # D (3)
    [(5, 5)],  # E (4)
    [(3, 6), (2, 4), (4, 5)]   # F (5)
]

# Prim's Algorithm 시작 (정점 0 = A에서 시작)
prim(graph_list, 0)
