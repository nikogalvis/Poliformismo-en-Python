class Menu_item:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self._name = name
        self._price = price
        self._quantity = quantity

    def name(self):
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name

    def price(self):
        return self._price

    def set_price(self, new_price: float):
        self._price = abs(new_price)

    def quantity(self):
        return self._quantity

    def set_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("How funny, get out of my restaurant, NOW")
        self._quantity = new_quantity

    def total_price(self):
        return self._price * self._quantity

    def discount(self):
        return self.total_price()

    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Beer(Menu_item):
    def discount(self):
      if(self.quantity() % 6 == 0):
        return self.total_price() * 0.9
      else: 
        return self.total_price()

    def __repr__(self):
        return f"Beer {self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Juice(Menu_item):
    def discount(self):
      if(self.total_price() > 30000):
        return self.total_price() * 0.95
      else: 
        return self.total_price()

    def __repr__(self):
        return f"Juice Flavor {self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Dessert(Menu_item):
    def discount(self):
      if(self._name == "Chocolate Cake"): #? Its because there are so much chocolate cake (and i dont like it) 
        return self.total_price() * 0.5
      else: 
        return self.total_price()


    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Fried_Chicken_Bucket(Menu_item):
    def discount(self):
        return self.total_price() * 0.9

    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Coffee(Menu_item):
    def discount(self):
      if(self.quantity() >= 3):
        return self.total_price() * 2/3
      else: 
        return self.total_price()

    def __repr__(self):
        return f"Coffee {self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Sandwich(Menu_item):
    def discount(self):
        return self.total_price() * 3/4
    
    def __repr__(self):
        return f"Sandwich {self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Pizza(Menu_item):
    def __init__(self, size: str, price: float, quantity: int = 1):
        super().__init__(name=f"{size} Pizza", price=price, quantity=quantity)

    def discount(self):
      if(self._name == "Large Pizza"): #? Good for family :D
        return self.total_price() * 0.5
      else: 
        return self.total_price()

    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Salad(Menu_item):
    def __repr__(self):
        return f"Salad {self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Water(Menu_item):
    def discount(self):
      if(self.quantity() >= 10):
        return self.total_price() * 0.9
      else: 
        return self.total_price() 

    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class IceCream(Menu_item):
    def __init__(self, flavor: str, price: float, quantity: int = 1):
        super().__init__(name=f"Ice Cream ({flavor})", price=price, quantity=quantity)

    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Soup(Menu_item):
    def __init__(self, variety: str, price: float, quantity: int = 1):
        super().__init__(name=f"{variety} Soup", price=price, quantity=quantity)

    def discount(self):
      if(self.quantity()  > 5):
        return self.total_price() * 0.95
      else: 
        return self.total_price()

    def __repr__(self):
        return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"


class Order:
    def __init__(self):
        self.items = []


    def add_item(self, item: Menu_item):
        self.items.append(item)

    def calculate_total(self):
      total = 0
      beer = False
      juice = False
      chicken = False
      water = False
      icecream = False

      for item in self.items:
          total += item.discount()
          if isinstance(item, Beer):
            beer = True
          if isinstance(item, Juice):
            juice = True
          if isinstance(item, Fried_Chicken_Bucket):
            chicken = True
          if isinstance(item, Water):
              water = True
          if isinstance(item, IceCream):
              icecream = True

      if (beer and chicken and icecream and water and juice): #* You just bought all the food, i will give you a discount
        total *= 0.95
      return total

    def show_order(self):
      print("Order summary:")
      for item in self.items:
        print(item)
      print(f"Total: ${self.calculate_total():,.2f}")

class Payment():
  def __init__(self, payment_mode: str, quantity: float):
      self.payment_mode = payment_mode
      self.quantity = quantity
  
  def paid(self, debt: float) -> str:
    if(self.payment_mode == "Virtual"):
      if(self.quantity >= debt):
         return "Thank you for your paid"
      elif(self.quantity < debt):
         return "Invalid Paid, no funds"
    elif(self.payment_mode == "Cash"):
      if(self.quantity >= debt):
         return f"Thank you for your paid, your change is: {(debt - self.quantity)*(-1)}$"
      elif(self.quantity < debt):
         return f"Hey, there is not enoguh money, you still owe me {debt - self.quantity}$"
    else:
       raise ValueError("This is not a valid method paid")
      

if __name__ == "__main__":
    order = Order()

    order.add_item(Beer("Corona", 5000, 6))                # descuento 10% por 6 cervezas
    order.add_item(Juice("Mango", 16000, 2))               # total 32,000 > 30,000 → 5% descuento
    order.add_item(Fried_Chicken_Bucket("Family", 25000))  # 10% descuento siempre
    order.add_item(Water("Bottle of Water", 1000, 10))     # 10% descuento por cantidad >= 10
    order.add_item(IceCream("Vanilla", 3000, 2))           # sin descuento
    order.add_item(Pizza("Large", 35000, 1))               # 50% descuento por ser Large
    order.add_item(Salad("Caesar", 7000, 1))               # sin descuento
    order.add_item(Coffee("Latte", 6000, 3))               # 3 cafés → 2/3 del precio total
    order.add_item(Soup("Tomato", 4000, 6))                # más de 5 sopas → 5% descuento
    order.add_item(Sandwich("Club", 8000, 1))              # siempre 25% descuento
    order.add_item(Dessert("Chocolate Cake", 5000, 1))     # 50% descuento por ser torta de chocolate

    order.show_order()

    # Simulando pago
    total = order.calculate_total()
    print("\n--- Payment ---")
    payment = Payment("Cash", total - 2000)  # paga en efectivo con 2000 de sobra
    print(payment.paid(total))
