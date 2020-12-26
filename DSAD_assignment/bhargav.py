#DSAD
lines_array = []
townpeoplecount = -1
graph = None
dayZereoInfectedPeople = []
Nodes_list = []
Unique_Nodes_list = []


def unique(list1):
    # insert the list to the set 
    list_set = set(list1)
    # convert the set to the list 
    unique_list = (list(list_set))

    return unique_list


class Graph:
    def __init__(self, noodes):
        self.nodes = noodes
        self.friends_list = {}
        for node in self.nodes:
            self.friends_list[node] = []

    def add_friends(self, u, v):
        if len(v.strip()) > 0:
            self.friends_list[u].append(v)
            self.friends_list[v].append(u)
            self.friends_list[v] = unique(self.friends_list[v])
            self.friends_list[u] = unique(self.friends_list[u])

    def degree(self, node):
        deg = len(self.friends_list[node])
        return deg

    def print_friends_Path(self, value):
        print(self.friends_list[value])

    # def get_paths
    def print_friends_list(self):
        for node in self.nodes:
            print(node, "->", self.friends_list[node])

    def ShortPath(self, sourcePerson, destPerson):
        explored = []

        # Queue for traversing the  
        # graph in the BFS 
        queue = [[sourcePerson]]

        # If the desired node is  
        # reached 
        if sourcePerson == destPerson:
            return ["UnKnown"]

            # Loop to traverse the graph
        # with the help of the queue 
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Codition to check if the 
            # current node is not visited 
            if node not in explored:
                neighbours = self.friends_list[node]

                # Loop to iterate over the  
                # neighbours of the node 
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the  
                    # neighbour node is the goal 
                    if neighbour == destPerson:
                        return new_path

                explored.append(node)

                # Condition when the nodes
        # are not connected 

        return ["UnKnown"]



def findInfectedPath(**kwargs):
    global graph
    list_y = []
    for key, value in kwargs.items():
        for iperson in dayZereoInfectedPeople:
            path = graph.ShortPath(iperson.strip().title(), value.strip().title())

            list_x = [len(path), path]
            list_y.append(list_x)
            print(list_y)
            print("Infection Path to " + value + " is :", end="")
            print(*path, sep='->')

            #infect_person = len(path)
            #infect_person = infect_person.append(path)


def findInfectedPerson(**kwargs):
    global graph
    for key, value in kwargs.items():
        for iperson in dayZereoInfectedPeople:
            print("Infected people on day " + str(value) + " is :", end="")
            print(str(graph.degree(iperson.strip().title())))


def findInfectionPeriod(**kwargs):
    global graph
    for key, value in kwargs.items():
        for iperson in dayZereoInfectedPeople:
            path = graph.ShortPath(iperson.strip().title(), value.strip().title())
            print("Infection Period of " + value + " is : ", end="")
            if len(path) - 1 == 0:
                print("Not Infected")
            else:
                print(len(path) - 1)


def file_read(fname):
    with open(fname, encoding="utf8") as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            lines_array.append(line)


def createTownGraph():
    global graph
    global dayZereoInfectedPeople
    file_read('inputPS9.txt')
    res = [int(i) for i in lines_array[0].split() if i.isdigit()]
    # Total Town people
    townpeoplecount = res[0]

    # Get Townpeople count
    skip = (len(lines_array) - townpeoplecount - 1)

    # Town People Data
    for person in lines_array[1:-1 * skip]:
        data = person.split(':')
        key = data[0].strip().title()
        Nodes_list.append(key)
        keylist = data[1].split(',')
        for friend in keylist:
            if len(friend.strip()) > 0:
                Nodes_list.append(friend.strip().title())

    Unique_Nodes_list = unique(Nodes_list)
    graph = Graph(Unique_Nodes_list)

    for person in lines_array[1:-1 * skip]:
        data = person.split(':')
        key = data[0].strip().title()
        keylist = data[1].split(',')
        for friend in keylist:
            graph.add_friends(key, friend.strip().title())
    graph.print_friends_list()

    print('Graph Created')

    # Day 0 Infection oeople
    data = lines_array[townpeoplecount + 1].split(":")
    dayZereoInfectedPeople = data[1].split(",")

    # Questions Loop
    for element in lines_array[skip + 3:]:
        exec(element)


createTownGraph()
