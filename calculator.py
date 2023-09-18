import math
while True:
    print("Выберите тип операции: +, -, *, /, expon, sqrt, factorial, sin, cos, tan, exit")
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
    elif opertype == "expon":
        num1 = float(input("Введите число"))
        num2 = int(input("Введите степень"))
        num = num1
        try:
            float(num1), int(num2)
        except:
            print("Неправильно введены числа")
            continue
        for i in range(num2-1):
            num = num*num1
        if num2 == 0:
            num = 1
        print(num)
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
        num = float(input("Введите число"))
        try:
            float(num1)
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