import matplotlib.pyplot as plt
import networkx as nx


def read_graph():
    f = open('C:/Users/Sergey/PycharmProjects/untitled2/17032016/towns.txt', 'r')
    G = {}
    for line in f:
        a, b, weight = line.split()
        if a not in G:
            G[a] = {b: {'weight': int(weight)}}
        else:
            G[a][b] = {'weight': int(weight)}
        if b not in G:
            G[b] = {a: {'weight': int(weight)}}
        else:
            G[b][a] = {'weight': int(weight)}
    f.close()
    return G


def DFS (graph, start, called, dfs_edges):
    called.add(start)
    for neighbour in graph[start]:
        if neighbour not in called:
            dfs_edges.append((start, neighbour))
            DFS(graph, neighbour, called, dfs_edges)


def BFS (graph, start, fired, bfs_edges):
    Q = [start]
    fired.add(start)
    while len(Q) != 0:
        current = Q.pop(0)
        for neighbour in graph[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Q.append(neighbour)
                bfs_edges.append((current, neighbour))

graph = read_graph()
G = nx.Graph(graph)

start_city = G.nodes()[0]
print(start_city)

pos = nx.fruchterman_reingold_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=[start_city], node_color='r', node_size=100, alpha=0.8)

nx.draw_networkx_nodes(G, pos, nodelist=[node for node in G.nodes() if node != start_city],
                       node_color='g',
                       node_size=50,
                       alpha=0.7)

nx.draw_networkx_labels(G, pos, font_size=16)

dfs_edges = []
DFS(graph, start_city, set(), dfs_edges)

nx.draw_networkx_edges(G, pos, width=1, alpha=0.35, edge_color='black')

nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, width=3, alpha=1, edge_color='b')

bfs_edges = []
BFS(graph, start_city, set(), bfs_edges)

nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, width=4, alpha=0.5, edge_color='r')

plt.axis('off')
plt.show()

if len(dfs_edges)+1 == len(G):
    print('graph is connected')
else:
    print('graph is not connected')


def dejkstra(G, start):
    shortest_path = {vertex: {'weight': float('+inf')} for vertex in G}
    shortest_path[start]['weight'] = 0
    queue = [start]
    while len(queue) != 0:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current]['weight'] + G[current][neighbour]['weight']
            if offering_shortest_path < shortest_path[neighbour]['weight']:
                shortest_path[neighbour]['weight'] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path

dict_way = dejkstra(graph, start_city)
print(dict_way)


def find_shortest_way(G, first, current, way=[]):
    dict_way = dejkstra(graph, first)
    s = 0
    friend = [current]
    while len(friend) != 0:
        for neighbour in G[current]:
            if s == 0:
                if G[current][neighbour]['weight'] == dict_way[current]['weight'] - dict_way[neighbour]['weight']:
                    way.append([current, neighbour])
                    friend.append(neighbour)
                    s = 1
                    if neighbour == first:
                        return way
        s = 0
        current = friend.pop(-1)


first_town, last_town = input(), input()
way = find_shortest_way(graph, first_town, last_town)
print(first_town, last_town, way)

pos = nx.fruchterman_reingold_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=[first_town, last_town], node_color='r', node_size=50, alpha=0.8)

nx.draw_networkx_nodes(G, pos, nodelist=[node for node in G.nodes() if (node != first_town) and (node != last_town)],
                       node_color='g',
                       node_size=50,
                       alpha=0.7)

nx.draw_networkx_labels(G, pos, font_size=16)

nx.draw_networkx_edges(G, pos, width=1, alpha=0.35, edge_color='black')

nx.draw_networkx_edges(G, pos, edgelist=way, width=3, alpha=1, edge_color='r')

plt.axis('off')
plt.show()

