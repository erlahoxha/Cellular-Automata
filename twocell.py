import os

class CellularAutomaton:
    def __init__(self):
        # Initial seed with a single "1" in the middle
        self.current_state = "0" * 120 + "1" + "0" * 120
        self.next_state = ""
        self.rule_set = "01101110"  # Here you can change the rule set
        self.cell_count = len(self.current_state)
        self.dead_cell = "\033[0;47m \033[0m"  # white square
        self.alive_cell = "\033[0;40m \033[0m" # black square

    def run(self):
        while True:
            self.display()
            self.compute_next_state()

    def display(self):
        # Prints the automaton state visually
        print("".join(self.alive_cell if cell == "1" else self.dead_cell for cell in self.current_state))
        # os.system('clear')  # Uncomment to clear screen between generations

    def compute_next_state(self):
        self.next_state = ""  # Reset next state
        for i in range(self.cell_count):
            left = self.current_state[i - 1] if i > 0 else self.current_state[-1]
            center = self.current_state[i]
            right = self.current_state[i + 1] if i < self.cell_count - 1 else self.current_state[0]
            pattern = left + center + right
            self.next_state += self.apply_rule(pattern)
        self.current_state = self.next_state

    def apply_rule(self, neighborhood):
        # Maps binary patterns to rule output
        patterns = {"111": 0, "110": 1, "101": 2, "100": 3, "011": 4, "010": 5, "001": 6, "000": 7}
        return self.rule_set[patterns[neighborhood]]

if __name__ == "__main__":
    automaton = CellularAutomaton()
    automaton.run()

