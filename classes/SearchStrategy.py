class Node:
    def __init__(self, state, direction, action=None, parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.direction = direction

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def __lt__(self, other):
        return self.state.x < other.state.y and self.state.y < other.state.y

    def succ(self, tuple_grid):
        x = self.state[0]
        y = self.state[1]
        neighbours = []

        #lewy sasiad
        if x > 0 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = "Go"
            elif self.direction == "Right":
                decision = ["rotate Left", "rotate Left", "Go"]
            elif self.direction == "Up":
                decision = ["rotate Left", "Go"]
            elif self.direction == "Down":
                decision = ["rotate Right", "Go"]

            neighbours.append((decision, (x - 1, y), "Left"))

        #gorny sasiad
        if y > 0 and (x, y) in tuple_grid:


            if self.direction == "Left":
                decision = ["rotate Right", "Go"]
            elif self.direction == "Right":
                decision = ["rotate Left", "Go"]
            elif self.direction == "Up":
                decision = "Go"
            elif self.direction == "Down":
                decision = ["rotate Left", "rotate Left", "Go"]

            neighbours.append((decision, (x, y - 1), "Up"))


        #prawy sasiad
        if x < 16 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = ["rotate Right", "rotate Right", "Go"]
            elif self.direction == "Right":
                decision = "Go"
            elif self.direction == "Up":
                decision = ["rotate Right", "Go"]
            elif self.direction == "Down":
                decision = ["rotate Left", "Go"]

            neighbours.append((decision, (x + 1, y), "Right"))

        #dolny sasiad
        if y < 16 and (x, y) in tuple_grid:

            if self.direction == "Left":
                decision = ["rotate Left", "Go"]
            elif self.direction == "Right":
                decision = ["rotate Right", "Go"]
            elif self.direction == "Up":
                decision = ["rotate Left", "rotate Left", "Go"]
            elif self.direction == "Down":
                decision = "Go"

            neighbours.append((decision, (x, y + 1), "Down"))


        #print(neighbours)
        return neighbours

def bfs(istate, goal_test, direction, tuple_grid):
    fringe = []
    explored = []
    path = []
    go = Node(istate, direction)
    fringe.append(go)

    while True:
        if not fringe:
            return False

        elem = fringe.pop(0)
        if elem.state == goal_test:
            while elem.parent is not None:
                if type(elem.action) == list:
                    for actions in elem.action:
                        path.append(actions)
                else:
                    path.append(elem.action)
                elem = elem.parent

            path.reverse()
            return path

        explored.append(elem)

        for action, state, direction_succ in elem.succ(tuple_grid):
            fringe_states = []
            explored_states = []

            for elements in explored:
                explored_states.append(elements.state)
            for elements in fringe:
                fringe_states.append(elements.state)

            if state not in explored_states and state not in fringe_states:
                x = Node(state, direction_succ)
                x.parent = elem
                x.action = action
                fringe.append(x)




class State:
    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation

    def get_position(self):
        return self.x, self.y, self.rotation

    def get_point(self):
        return self.x, self.y

    def get_rotation(self):
        return self.rotation

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def set_rotation(self, rotation):
        self.rotation = rotation
