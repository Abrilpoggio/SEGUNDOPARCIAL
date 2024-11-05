class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, character):
        if character not in self.vertices:
            self.vertices[character] = []
            self.edges[character] = {}

    def add_edge(self, character1, character2, episodes):
        if character1 in self.vertices and character2 in self.vertices:
            self.edges[character1][character2] = episodes
            self.edges[character2][character1] = episodes  
    def min_spanning_tree(self, start_character):
        visited = set()
        mst_edges = []
        min_edges = [(0, start_character, None)]  

        while min_edges:
            weight, current_vertex, from_vertex = heapq.heappop(min_edges)
            if current_vertex not in visited:
                visited.add(current_vertex)
                if from_vertex is not None:
                    mst_edges.append((from_vertex, current_vertex, weight))

                for neighbor, edge_weight in self.edges[current_vertex].items():
                    if neighbor not in visited:
                        heapq.heappush(min_edges, (edge_weight, neighbor, current_vertex))

        return mst_edges

    def has_character_in_mst(self, mst, character):
        for from_vertex, to_vertex, weight in mst:
            if character in (from_vertex, to_vertex):
                return True
        return False

    def max_shared_episodes(self):
        max_episodes = 0
        characters = (None, None)

        for character1 in self.edges:
            for character2, episodes in self.edges[character1].items():
                if episodes > max_episodes:
                    max_episodes = episodes
                    characters = (character1, character2)

        return max_episodes, characters



graph = Graph()
characters = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for character in characters:
    graph.add_vertex(character)


graph.add_edge("Luke Skywalker", "Darth Vader", 5)
graph.add_edge("Luke Skywalker", "Yoda", 3)
graph.add_edge("Yoda", "Darth Vader", 1)
graph.add_edge("Boba Fett", "Darth Vader", 4)
graph.add_edge("C-3PO", "Leia", 6)
graph.add_edge("Leia", "Rey", 2)
graph.add_edge("Rey", "Kylo Ren", 7)
graph.add_edge("Chewbacca", "Han Solo", 5)
graph.add_edge("R2-D2", "C-3PO", 5)
graph.add_edge("BB-8", "Rey", 3)


import heapq

mst = graph.min_spanning_tree("Yoda")
contains_yoda = graph.has_character_in_mst(mst, "Yoda")


max_episodes, characters_shared = graph.max_shared_episodes()


print("MST:", mst)
print("¿Contiene a Yoda en el MST?", contains_yoda)
print("Máximo número de episodios compartidos:", max_episodes, "entre", characters_shared)
