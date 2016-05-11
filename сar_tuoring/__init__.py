class TuringMachine:
    def __init__(self):
        with open('instructions.txt') as f:
            instructions = f.readlines()
        self.instructions = {}
        for one in instructions:
            current = one.split()
            self.instructions[current[0]] = current[1]

        with open('information.txt') as f:
            information = f.readline()
        self.line = ['B']
        for one in information:
            self.line.append(one)
        self.line.append('B')

    def action(self):
        state = 'q1'
        number = 1
        while state != 'qZ':
            symbol = self.line[number]
            current_state = str(symbol) + state
            current_instruction = self.instructions[current_state]
            if current_instruction[0] != 'B':
                self.line[number] = current_instruction[0]
            state = current_instruction[1:3]
            if current_instruction[3:] == 'R':
                number += 1
            elif current_instruction[3:] == 'L':
                number -= 1
        for i in self.line[1:-1]:
            print(i, end='')

Turing = TuringMachine()
Turing.action()