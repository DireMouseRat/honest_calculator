YES = ['yes', 'y', 'Yes', 'Y']
NO = ['no', 'n', 'No', 'n']


class Calculator:
    ask_for_equation = "Enter an equation\n"
    ask_store_or_discard_result = "Do you want to store the result? (y / n):\n"
    ask_continue_or_exit = "Do you want to continue calculations? (y / n):\n"
    input_is_alpha = "Do you even know what numbers are? Stay focused!"
    input_is_not_operator = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    input_is_division_by_zero = "Yeah... division by zero. Smart move..."

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.result = 0.0
        self.operator = ''
        self.memory = []
        self.start_calculator()

    def get_valid_input(self):
        while True:
            left, middle, right = input(self.ask_for_equation).split()
            if left.isalpha() or right.isalpha():
                print(self.input_is_alpha)
            elif middle not in ['+', '-', '*', '/']:
                print(self.input_is_not_operator)
            elif middle == '/' and float(right) == 0:
                print(self.input_is_division_by_zero)
            else:
                self.x = float(left)
                self.y = float(right)
                self.operator = str(middle)
                break

    def calculate_operation(self):
        if self.operator == '+':
            self.result = self.x + self.y
        elif self.operator == '-':
            self.result = self.x - self.y
        elif self.operator == '*':
            self.result = self.x * self.y
        elif self.operator == '/':
            self.result = self.x / self.y

    def display_result(self):
        print(self.result)

    def store_or_discard(self):
        if input(self.ask_store_or_discard_result) in YES:
            self.memory.append(self.result)

    def start_calculator(self):
        self.get_valid_input()
        self.calculate_operation()
        self.display_result()
        self.store_or_discard()
        self.continue_or_exit()

    def continue_or_exit(self):
        if input(self.ask_continue_or_exit) in YES:
            self.start_calculator()


Calculator()
