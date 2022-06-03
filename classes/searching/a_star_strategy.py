class StarNode:
    def __init__(self, state, direction, action=None, parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.direction = direction
        self.g = 0
        self.h = 0
        self.f = 0

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def __eq__(self, other):
        return self.state == other.state

    def succ(self, tuple_grid):
        x = self.state[0]
        y = self.state[1]
        neighbours = []

        # lewy sasiad
        if x > 0 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = ["Go"]
            elif self.direction == "Right":
                decision = ["rotate Left", "rotate Left", "Go"]
            elif self.direction == "Up":
                decision = ["rotate Left", "Go"]
            elif self.direction == "Down":
                decision = ["rotate Right", "Go"]

            neighbours.append(StarNode((x - 1, y), "Left", decision))

        # gorny sasiad
        if y > 0 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = ["rotate Right", "Go"]
            elif self.direction == "Right":
                decision = ["rotate Left", "Go"]
            elif self.direction == "Up":
                decision = ["Go"]
            elif self.direction == "Down":
                decision = ["rotate Left", "rotate Left", "Go"]

            neighbours.append(StarNode((x, y - 1), "Up", decision))

        # prawy sasiad
        if x < 16 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = ["rotate Right", "rotate Right", "Go"]
            elif self.direction == "Right":
                decision = ["Go"]
            elif self.direction == "Up":
                decision = ["rotate Right", "Go"]
            elif self.direction == "Down":
                decision = ["rotate Left", "Go"]

            neighbours.append(StarNode((x + 1, y), "Right", decision, ))

        # dolny sasiad
        if y < 16 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = ["rotate Left", "Go"]
            elif self.direction == "Right":
                decision = ["rotate Right", "Go"]
            elif self.direction == "Up":
                decision = ["rotate Left", "rotate Left", "Go"]
            elif self.direction == "Down":
                decision = ["Go"]

            neighbours.append(StarNode((x, y + 1), "Down", decision))

        return neighbours


def heuristic_fun(start, goal):
    h = abs(start.state[0] - goal.state[0]) + abs(start.state[1] - goal.state[1])
    return h


def a_star_strategy(start, goal, direction, map, mapbycost):
    open_list = []
    closed_list = []

    start_node = StarNode(start, direction)
    end_node = StarNode(goal, None)
    start_node.h = heuristic_fun(start_node, end_node)
    start_node.g = 0
    start_node.f += start_node.g + start_node.h

    open_list.append(start_node)

    while len(open_list) != 0:
        current_node = open_list[0]
        current_node_number = 0
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_node_number = index
        open_list.pop(current_node_number)
        closed_list.append(current_node)

        if current_node.state == end_node.state:
            path = []
            current = current_node
            while current is not None:
                 if current.action is not None:
                     current.action.reverse()
                     for each_action in current.action:
                         path.append(each_action)
                 current = current.parent
            return path[::-1]

        for node_successor in current_node.succ(map):
            len_action = 0
            if current_node.action is not None:
                len_action = len(current_node.action)
            succesor_current_cost = current_node.g + mapbycost[node_successor.state[0]][node_successor.state[1]] + len_action
            if node_successor in open_list:
                if node_successor.g <= succesor_current_cost:
                    continue
            elif node_successor in closed_list:
                if node_successor.g <= succesor_current_cost:
                    continue
                else:
                    closed_list.remove(node_successor)
                    open_list.append(node_successor)
            else:
                node_successor.h = heuristic_fun(node_successor, end_node)
                open_list.append(node_successor)
            node_successor.g = succesor_current_cost
            node_successor.f += node_successor.g + node_successor.h
            node_successor.parent = current_node
        closed_list.append(current_node)
    if(current_node!=end_node):
        return "ERROR"