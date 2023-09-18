import math
while True:
    print("Выберите тип операции: +, -, *, /, **, sqrt, factorial, sin, cos, tan, exit")
    opertype = input("")
    if opertype == "+" or opertype == "-" or opertype == "*" or opertype == "/":
        num1 = input("Введите первое число")
        num2 = input("Введите второе число")
        try:
            float(num1), float(num2)
        except:
            print("Неправильно введены числа")
            continue
        try:
            oper = num1 + opertype + num2
            print(eval(oper))
        except:
            print("Нельзя делить на ноль")
    elif opertype == "**":
        num1 = input("Введите число")
        num2 = input("Введите степень")
        try:
            num1 = float(num1)
            num2 = int(num2)
            print(num1**num2)
        except:
            print("Неправильно введены числа")
            continue
    elif opertype == "sqrt" or opertype == "factorial":
        num = input("Введите число")
        try:
            float(num)
        except:
            print("Неправильно введены числа")
            continue
        oper = "math."+opertype+"("+ num + ")"
        print(eval(oper))
    elif opertype == "sin" or opertype == "cos" or opertype == "tan":
        num = input("Введите число")
        try:
            num = float(num)
        except:
            print("Неправильно введены числа")
            continue
        num = math.radians(num)
        oper = "math."+opertype+"("+ str(num) + ")"
        print(eval(oper))
    elif opertype == "exit":
        break
    else:
        print("Неизвестная операция")
