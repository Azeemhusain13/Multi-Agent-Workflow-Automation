import networkx as nx

class Workflow:
    def __init__(self):
        self.g = nx.DiGraph()
    def add_node(self, name, agent):
        self.g.add_node(name, agent=agent)
    def add_edge(self, a, b):
        self.g.add_edge(a, b)
    def run(self, memory):
        order = list(nx.topological_sort(self.g))
        for node in order:
            agent = self.g.nodes[node]['agent']
            memory = agent(memory)
            trace = memory.get('trace', [])
            trace.append(node)
            memory['trace'] = trace
        return memory
