from random import randint

a = randint(1 , 10)


while True:
    b= int(input("Введи число "))
    if b == a:
        print("Вгадав")
        break
    elif a<b:
        print("Число меньше")
    elif a>b:
        print("Число більше")    
    else:
        print("Попробуй ше раз")