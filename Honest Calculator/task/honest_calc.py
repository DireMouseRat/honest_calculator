class PassiveAggressiveCalculator:
    ask_for_equation = "Enter an equation\n"
    ask_store_result = "Do you want to store the result? (y / n):\n"
    ask_continue_calculations = "Do you want to continue calculations? (y / n):\n"
    input_is_alpha = "Do you even know what numbers are? Stay focused!"
    input_is_not_operator = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    input_is_division_by_zero = "Yeah... division by zero. Smart move..."
    msg_lazy = " ... lazy"
    msg_very_lazy = " ... very lazy"
    msg_very_very_lazy = " ... very, very lazy"
    msg_you_are = "You are"

    def __init__(self):
        self.x = 0
        self.y = 0
        self.result = 0
        self.memory = 0
        self.operator = ''
        self.start_calculator()

    def start_calculator(self):
        continue_calculating = True
        while continue_calculating:
            self.get_valid_input()
            self.shame_user()
            if self.division_by_zero():
                continue
            self.calculate_operation()
            self.display_result()
            self.store_or_discard()
            continue_calculating = self.continue_calculations()

    def get_valid_input(self):
        valid = False
        while not valid:
            left, middle, right = input(self.ask_for_equation).split()
            left = str(self.memory) if left == 'M' else left
            right = str(self.memory) if right == 'M' else right
            if left.isalpha() or right.isalpha():
                print(self.input_is_alpha)
            elif middle not in ['+', '-', '*', '/']:
                print(self.input_is_not_operator)
            else:
                self.x = float(left) if '.' in left else int(left)
                self.y = float(right) if '.' in right else int(right)
                self.operator = str(middle)
                valid = True

    def calculate_operation(self):
        if self.operator == '+':
            self.result = self.x + self.y
        elif self.operator == '-':
            self.result = self.x - self.y
        elif self.operator == '*':
            self.result = float(self.x * self.y)
        elif self.operator == '/':
            self.result = self.x / self.y
        self.result = float(self.result)

    def display_result(self):
        print(self.result)

    def store_or_discard(self):
        valid = False
        while not valid:
            user_response = input(self.ask_store_result)
            if user_response == 'y':
                self.memory = self.result
                valid = True
            elif user_response == 'n':
                valid = True

    def continue_calculations(self):
        while True:
            user_response = input(self.ask_continue_calculations)
            if user_response == 'y':
                return True
            elif user_response == 'n':
                return False

    def shame_user(self):
        msg = ''
        x = self.x
        y = self.y
        o = self.operator
        if self.is_one_digit(x) and self.is_one_digit(y):
            msg += self.msg_lazy
        if (x == 1 or y == 1) and o == '*':
            msg += self.msg_very_lazy
        if (x == 0 or y == 0) and (o == '*' or o == '+' or o == '-'):
            msg += self.msg_very_very_lazy
        if msg != '':
            msg = self.msg_you_are + msg
            print(msg)

    def is_one_digit(self, v):
        if '.' in str(v) and str(v)[2] == 0:
            return True
        if -10 < int(v) < 10 and '.' not in str(v):
            return True
        return False

    def division_by_zero(self):
        if self.operator == '/' and self.y == 0:
            print(self.input_is_division_by_zero)
            return True
        return False


PassiveAggressiveCalculator()
