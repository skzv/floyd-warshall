class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.edges = set()
        self.weights = {}

    def add_edge(self, u, v, c):
        e = (u, v)
        self.edges.add(e)
        self.weights[e] = c

    def has_edge(self, u, v):
        e = (u, v)
        return e in self.edges

    def get_edge_weight(self, u, v):
        e = (u, v)
        return self.weights[e]


def read_graph(filename):
    file = open('data/' + filename, 'r')
    n = int(file.readline().split(' ')[0])
    g = Graph(n)

    for line in file:
        tokens = line.rstrip('\n').split(' ')
        u = int(tokens[0])
        v = int(tokens[1])
        c = int(tokens[2])
        g.add_edge(u, v, c)

    return g


def floyd_marshall(g):
    n = g.num_vertices
    A = [[[0] * n] * n] * n

    # base cases (k=0)
    for v in range(1, n + 1):
        for w in range(1, n + 1):
            if v == w:
                A[0][v - 1][w - 1] = 0
            elif g.has_edge(v, w):
                A[0][v - 1][w - 1] = g.get_edge_weight(v, w)
            else:
                A[0][v - 1][w - 1] = 1_000_000_000  # inf

    # systematically solve all sub-problems
    for k in range(1, n + 1):
        print('{0}/{1}'.format(k, n))
        for v in range(1, n + 1):
            for w in range(1, n + 1):
                A[k - 1][v - 1][w - 1] = min(A[k - 2][v - 1][w - 1], A[k - 2][v - 1][k - 1] + A[k - 2][k - 1][w - 1])

    # check for negative cycle
    for v in range(1, n + 1):
        if A[n - 1][v - 1][v - 1] < 0:
            # Contains negative cycle
            return None

    return A[n - 1][:][:]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g1 = read_graph("G1.txt")
    d1 = floyd_marshall(g1)
    s1 = min(d1)

    g2 = read_graph("G2.txt")
    d2 = floyd_marshall(g2)
    s2 = min(d2)

    g3 = read_graph("G3.txt")
    d3 = floyd_marshall(g3)
    s3 = min(d3)

    print(s1)
    print(s2)
    print(s3)
