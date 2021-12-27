# https://www.acmicpc.net/problem/1647
def find_parent(parent,x) : #연결된 노드중 부모노드 찾기
    if(parent[x] != x ):
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a >b  :
        parent[a] = b
    else :
        parent[b] = a

v,e = map(int,input().split())
parent = [0]*(v+1)
edges = []
result = 0
for i in range(1,v+1):
    parent[i] = i

for i in range(e) :
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0

for edge in edges :
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        result +=cost
        last = cost
print(result -last)

