#hw2_5

class UnionFind:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be greater than 0")
        
        # 초기화: 각 노드는 자기 자신을 부모로 가리킴
        self.size = size
        self.num_components = size
        self.sz = [1] * size  # 각 컴포넌트의 크기 (랭크 대체)
        self.id = list(range(size))  # 부모를 나타내는 배열

    def find(self, p):
        # 경로 압축을 적용한 find 연산
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # 경로 압축
        while p != root:
            next_p = self.id[p]
            self.id[p] = root
            p = next_p

        return root

    def connected(self, p, q):
        # 두 노드가 같은 집합에 속하는지 여부를 반환
        return self.find(p) == self.find(q)

    def component_size(self, p):
        # 해당 노드가 속한 집합의 크기를 반환
        return self.sz[self.find(p)]

    def components(self):
        # 남은 집합의 개수를 반환
        return self.num_components

    def unify(self, p, q):
        # 두 노드를 같은 집합으로 합치기
        root1 = self.find(p)
        root2 = self.find(q)

        print(f"Before union: Node {p+1} root is {root1+1}, Node {q+1} root is {root2+1}")
        
        # 이미 같은 집합에 속하면 아무것도 안함
        if root1 == root2:
            print(f"Nodes {p+1} and {q+1} are already connected.")
            return

        # 작은 집합을 큰 집합에 합친다 (랭크 기반)
        if self.sz[root1] < self.sz[root2]:
            self.id[root1] = root2
            self.sz[root2] += self.sz[root1]
            print(f"Node {root1+1} is now pointing to {root2+1}")
        elif self.sz[root1] > self.sz[root2]:
            self.id[root2] = root1
            self.sz[root1] += self.sz[root2]
            print(f"Node {root2+1} is now pointing to {root1+1}")
        else:
            # 사이즈가 같을 때, 더 큰 번호가 루트가 되도록 한다
            if root1 < root2:
                self.id[root1] = root2
                self.sz[root2] += self.sz[root1]
                print(f"Node {root1+1} is now pointing to {root2+1}")
            else:
                self.id[root2] = root1
                self.sz[root1] += self.sz[root2]
                print(f"Node {root2+1} is now pointing to {root1+1}")

        # 컴포넌트의 수를 하나 줄임
        self.num_components -= 1

        # 연산 후 상태 출력
        print(f"After union: Node {p+1} root is {self.find(p)+1}, Node {q+1} root is {self.find(q)+1}")
        print(f"Parent array: {self.parent_as_str()}\n")

    def parent_as_str(self):
        # 각 노드의 부모 배열을 1-based로 출력하기 위한 함수
        return [p + 1 for p in self.id]

# 사용 예시
uf = UnionFind(8)

uf.unify(0, 1)  # union(1, 2)
uf.unify(2, 3)  # union(3, 4)
uf.unify(4, 5)  # union(5, 6)
uf.unify(6, 7)  # union(7, 8)
uf.unify(0, 3)  # union(1, 4)
uf.unify(5, 6)  # union(6, 7)
uf.unify(3, 4)  # union(4, 5)

# Find root of element 1
root_of_1 = uf.find(0)
print(f"Root of element 1: {root_of_1 + 1}")  # 출력할 때는 1-based로 변환
