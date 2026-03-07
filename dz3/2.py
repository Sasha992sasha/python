class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.suma = price*count

class Cart:
    def __init__(self):
        self.spisok = []

    def add(self , prod):
        self.spisok.append(prod)
    
    def remove(self,index):
        self.spisok.pop(index)
    
    def printer(self):
        for index, item in enumerate(self.spisok):
            print(f"{index}: {item.name}")

t1 = Product("Яблуко" , 20 , 1)
t2 = Product("Молоко" , 2 ,13)

cart = Cart()

cart.add (t1)
cart.add (t2)

cart.printer()
cart.suma()