while True:
    print("Enter an equation")
    x, operation, y = input().split()
    if x.isalpha() or y.isalpha():
        print("Do you even know what numbers are? Stay focused!")
    elif operation not in ["+", "-", "*", "/"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    else:
        break
