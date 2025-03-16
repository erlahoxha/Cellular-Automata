import os

class FiveCellAutomaton:
    def __init__(self):
        self.current_state = "0" * 120 + "1" + "0" * 120  # Initial seed with some "1"s scattered
        self.next_state = ""
        self.rule_set = "01101011011110101011001110101110"  # Here you can change the rule set
        self.cell_count = len(self.current_state)
        self.dead_cell = "\033[0;47m \033[0m" # white square
        self.alive_cell = "\033[0;40m \033[0m" # black square

    def run(self):
        while True:
            self.display()
            self.compute_next_state()

    def display(self):
        print("".join(self.alive_cell if cell == "1" else self.dead_cell for cell in self.current_state))

    def compute_next_state(self):
        self.next_state = ""
        for i in range(self.cell_count):
            # Determine neighborhood with wrapping
            left2 = self.current_state[(i - 2) % self.cell_count]
            left1 = self.current_state[(i - 1) % self.cell_count]
            center = self.current_state[i]
            right1 = self.current_state[(i + 1) % self.cell_count]
            right2 = self.current_state[(i + 2) % self.cell_count]
            pattern = left2 + left1 + center + right1 + right2
            self.next_state += self.apply_rule(pattern)
        self.current_state = self.next_state

    def apply_rule(self, neighborhood):
        patterns = {bin(i)[2:].zfill(5): i for i in range(32)}  # Generate binary mappings for 5-cell patterns
        return self.rule_set[patterns[neighborhood]]

if __name__ == "__main__":
    automaton = FiveCellAutomaton()
    automaton.run()


