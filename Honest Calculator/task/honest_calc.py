class Calculator:
    ask_for_equation = "Enter an equation\n"
    ask_store_result = "Do you want to store the result? (y / n):\n"
    ask_continue_calculations = "Do you want to continue calculations? (y / n):\n"
    input_is_alpha = "Do you even know what numbers are? Stay focused!"
    input_is_not_operator = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    input_is_division_by_zero = "Yeah... division by zero. Smart move..."

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.result = 0.0
        self.memory = 0.0
        self.operator = ''
        self.start_calculator()

    def get_valid_input(self):
        invalid = True
        while invalid:
            left, middle, right = input(self.ask_for_equation).split()
            left = str(self.memory) if left == 'M' else left
            right = str(self.memory) if right == 'M' else right
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
                invalid = False

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
        invalid = True
        while invalid:
            user_response = input(self.ask_store_result)
            if user_response == 'y':
                self.memory = self.result
                invalid = False
            elif user_response == 'n':
                invalid = False

    def start_calculator(self):
        continue_calculating = True
        while continue_calculating:
            self.get_valid_input()
            self.calculate_operation()
            self.display_result()
            self.store_or_discard()
            continue_calculating = self.continue_calculations()

    def continue_calculations(self):
        while True:
            user_response = input(self.ask_continue_calculations)
            if user_response == 'y':
                return True
            elif user_response == 'n':
                return False


Calculator()
