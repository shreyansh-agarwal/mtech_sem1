friends_list = {

}


gupton = ('sharman', 'roy', 'kumar', 'ray')
ray = ('ray', 'goldberg', 'arun', 'gupton')
sharman = ('gupton', 'panth', 'jaim')
kumar = 'gupton'
panth = 'kumar'
roy = ('gupton', 'goldberg')
goldberg =  ('roy', 'ray')
arun = ('jaim', 'ray')
goldi = ""
jaim = ('sharman', 'arun')


class Graph:
    def __init__(self, noodes):
        self.nodes = noodes
        self.friends_list = {}

        for node in self.nodes:
            self.friends_list[node] = []

    def add_friends(self, u, v):
        self.friends_list[u].append(v)
        self.friends_list[v].append(u)

    def degree(self, node):
        deg = len(self.friends_list[node])
        return deg

    def print_friends_list(self):
        for node in self.nodes:
            print(node, "->", self.friends_list[node])


nodes = ["gupton", "ray", "sharman", "roy", "panth", "kumar", "goldberg", "arun", "goldi", "jaim"]
graph = Graph(nodes)
#graph.print_friends_list()
graph.add_friends("gupton", "roy")
graph.add_friends("gupton", "sharman")
graph.add_friends("gupton", "ray")
graph.add_friends("gupton", "kumar")
graph.add_friends("ray", "goldberg")
graph.add_friends("ray", "arun")
graph.add_friends("sharman", "panth")
graph.add_friends("sharman", "jaim")
graph.add_friends("panth", "kumar")
graph.add_friends("goldberg", "roy")
graph.add_friends("arun", "jaim")


graph.print_friends_list()
print ("No of friends of roy: ", graph.degree("roy"))
print ("No of friends of jaim: ", graph.degree("jaim"))
