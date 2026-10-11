def BFS(n, m, s, t, edges):
    # Please write your algorithm here:
    # Return result as "yes" or "no" (lowercase).
    # Return layer as the BFS distance from s to t, or "inf" if unreachable.
    # If s == t, return "yes", 0.

    # .................................
    return result, layer


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
