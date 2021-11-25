MSG = ["Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):\n",
       "Do you want to continue calculations? (y / n):\n",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += MSG[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += MSG[7]
    if (v1 == 0 or v2 == 0) and v3 in ['*', '+', '-']:
        msg += MSG[8]
    if msg != '':
        print(MSG[9] + msg)


def is_one_digit(v):
    return -10 < v < 10 and int(v) == float(v)


operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

memory = 0

while True:
    print(MSG[0])
    x, oper, y = input().split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        check(x, y, oper)
        result = operations[oper](x, y)
        print(result)
        if input(MSG[4]) == "y":
            if is_one_digit(result):
                i = 10
                while True:
                    a = input(MSG[i])
                    if a == "y":
                        if i < 12:
                            i += 1
                        else:
                            memory = result
                            break
                    elif a == 'n':
                        break
            else:
                memory = result
        if input(MSG[5]) == "n":
            break
    except ValueError:
        print(MSG[1])
    except KeyError:
        print(MSG[2])
    except ZeroDivisionError:
        print(MSG[3])
