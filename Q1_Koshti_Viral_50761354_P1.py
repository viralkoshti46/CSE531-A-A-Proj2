def BFS(n, m, s, t, edges):
    adjacency = [[] for _ in range(n + 1)]

    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    distance = [-1] * (n + 1)
    queue = [s]
    front = 0
    distance[s] = 0

    while front < len(queue):
        u = queue[front]
        front += 1

        if u == t:
            return "yes", distance[t]

        for v in adjacency[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                queue.append(v)

    return "no", "inf"


def read_input():
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, s, t, edges


if __name__ == "__main__":
    n, m, s, t, edges = read_input()
    result, layer = BFS(n, m, s, t, edges)
    print(result)
    print(layer)
