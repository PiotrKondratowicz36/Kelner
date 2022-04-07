class Node:
    def __init__(self, state, action=None, parent=None):
        self.state = state
        self.parent = parent
        self.action = action

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
