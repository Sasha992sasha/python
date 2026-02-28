a = int(input("Число 1 "))
b = int(input("Число 2 "))

c = input("Дія ")

if c == "+":
    print(a+b)

elif c == "-":
    print(a-b)

elif c == "*":
    print(a*b)

elif c == "/":
    if b!=0:
        print(a/b)
    else:
        print("Ну ділить на 0 це моцно")

elif c == "**":
    print(a**b)

