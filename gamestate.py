
class GameState:
    def __init__(self):
        self.states = ["Main Menu", "Playing Game", "In Settings Page", "In Game Menu"]
        self.GAMESTATE = self.states[0]

    def set_gamestate(self, state):
        self.GAMESTATE = self.states[state]

    def get_gamestate(self):
        return self.GAMESTATE

    def get_states(self):
        return self.states