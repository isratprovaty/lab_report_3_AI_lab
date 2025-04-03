def is_safe(graph, colors, v, c):
    for i in range(len(graph)):
        if graph[v][i] and colors[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, colors, v):
    n = len(graph)
    if v == n:
        return True, colors

    for c in range(1, m + 1):
        if is_safe(graph, colors, v, c):
            colors[v] = c
            possible, result_colors = graph_coloring_util(graph, m, colors, v + 1)
            if possible:
                return True, result_colors
            colors[v] = 0

    return False, colors

def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n
    possible, result_colors = graph_coloring_util(graph, m, colors, 0)
    return possible, result_colors

if __name__ == "__main__":
    import sys
    case_number = 0
    while True:
        line1 = sys.stdin.readline().split()
        if not line1:
            break
        case_number += 1
        n = int(line1[0])
        m_edges = int(line1[1])
        k = int(line1[2])

        graph = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m_edges):
            edge = sys.stdin.readline().split()
            u = int(edge[0])
            v = int(edge[1])
            graph[u][v] = 1
            graph[v][u] = 1

        possible, coloring = graph_coloring(graph, k)

        if case_number == 1:
            print("Case#1Output:")
            if possible:
                print(f"Coloring Possible with {k} Colors")
                print(f"Color Assignment: {coloring}")
            else:
                print(f"Coloring Not Possible with {k} Colors")
        elif case_number == 2:
            print("\nCase#2Output:")
            if possible:
                print(f"Coloring Possible with {k} Colors")
                print(f"Color Assignment: {coloring}")
            else:
                print(f"Coloring Not Possible with {k} Colors")
        else:
            print(f"\nCase#{case_number}Output:")
            if possible:
                print(f"Coloring Possible with {k} Colors")
                print(f"Color Assignment: {coloring}")
            else:
                print(f"Coloring Not Possible with {k} Colors")
