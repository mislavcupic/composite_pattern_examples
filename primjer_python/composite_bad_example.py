# #u ovom primjeru je ista struktura Product, ali bez implementacije Box interfejsa
# class SimpleProduct:  
#     def __init__(self, title: str, price: float):
#         self._title = title
#         self._price = price

#     def calculate_price(self) -> float:
#         return self._price
    
# # ako želim novi tip producta, moram stvarati poseban tip da bih ga pospremio u poseban box jer ovaj product ima dodatni prop
# class MobilePhoneProduct:
#     def __init__(self, title: str, price: float, warranty: int):
#         self._title = title
#         self._price = price
#         self.warranty = warranty
#     def calculate_price(self) -> float:
#         return self._price
        

# # kada bih htio dodati kutije s drugim vrstama proizvoda, na primjer bananama, ili tenisicama, morao bih stvoriti novu klasu sličnu SimpleBox 
# class SimpleBox:
#     def __init__(self):
#         self._products = []  # Lista za pohranu proizvoda u tijelu konstruktora

#     def add_product(self, product: SimpleProduct):
#         self._products.append(product)

#     def calculate_total_price(self) -> float:
#         total_price = 0
#         for product in self._products:
#             total_price += product.calculate_price()
#         return total_price

#     def display_products(self):
#         print("Proizvodi u kutiji:")
#         for product in self._products:
#             print(f"- {product._title}: ${product.calculate_price():.2f}")
#         print(f"Ukupna cijena kutije: ${self.calculate_total_price():.2f}")

# """class MobilePhoneBox:
#     def __init__(self):
#         self._products = []  # Lista za pohranu proizvoda

#     def add_product(self, product: Product):
#         self._products.append(product)

#     def calculate_total_price(self) -> float:
#         total_price = 0
#         for product in self._products:
#             total_price += product.calculate_price()
#         return total_price

#     def display_products(self):
#         print("Proizvodi u kutiji:")
#         for product in self._products:
#             print(f"- {product._title}: ${product.calculate_price():.2f}")
#         print(f"Ukupna cijena kutije: ${self.calculate_total_price():.2f}")
# """
# if __name__ == "__main__":
#     # Stvaranje pojedinačnih proizvoda
#     product1 = SimpleProduct("Proizvod 1", 10.0)
#     product2 = SimpleProduct("Proizvod 2", 15.0)
#     product3 = SimpleProduct("Proizvod 3", 20.0)

   

#     # Stvaranje jednostavne kutije i dodavanje proizvoda
#     """pa kad bih htio dodati nove mobitele u kutiju bih trebao stvoriti posebno instancu MobilePhone kutije...
#     Ako želim da SimpleBox može raditi s MobilePhoneProduct, možda ću morati dodati dodatnu logiku unutar SimpleBox
#       da bih ispravno obradio novu klasu."""
#     box = SimpleBox()
#     box.add_product(product1)
#     box.add_product(product2)
#     box.add_product(product3)
#     # Ovo će izazvati grešku jer MobilePhoneProduct nije SimpleProduct - TypeError: SimpleBox.add_product() takes 2 positional arguments but 4 were given
#   #  box.add_product("Mobilni Telefon", 500, 12) 
#     #pa bismo za svaki novi tip produkta morali raditi posebne instance tipa proizvoda
#     #box.add_product(product=MobilePhoneProduct("Mobilni telefon",500,12))

#     # Ispis proizvoda i ukupne cijene
#     box.display_products()
# "Bad" structure without composite pattern

class SimpleProduct:  
    def __init__(self, title: str, price: float):
        self._title = title
        self._price = price

    def calculate_price(self) -> float:
        return self._price

    def display(self):
        return f"{self._title}: ${self._price:.2f}"

class MobilePhoneProduct:
    def __init__(self, title: str, price: float, warranty: int):
        self._title = title
        self._price = price
        self.warranty = warranty

    def calculate_price(self) -> float:
        return self._price

    def display(self):
        return f"{self._title}: ${self._price:.2f} (Warranty: {self.warranty} months)"

# Box that can only store SimpleProducts
class SimpleBox:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        if isinstance(product, SimpleProduct):
            self._products.append(product)
        else:
            raise TypeError("SimpleBox can only contain SimpleProduct instances")

    def calculate_total_price(self) -> float:
        return sum(product.calculate_price() for product in self._products)

    def display(self):
        product_details = "\n".join(f"- {product.display()}" for product in self._products)
        total_price = self.calculate_total_price()
        return f"SimpleBox:\n{product_details}\nTotal price: ${total_price:.2f}"

# A different box class that can store MobilePhoneProducts only
class MobilePhoneBox:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        if isinstance(product, MobilePhoneProduct):
            self._products.append(product)
        else:
            raise TypeError("MobilePhoneBox can only contain MobilePhoneProduct instances")

    def calculate_total_price(self) -> float:
        return sum(product.calculate_price() for product in self._products)

    def display(self):
        product_details = "\n".join(f"- {product.display()}" for product in self._products)
        total_price = self.calculate_total_price()
        return f"MobilePhoneBox:\n{product_details}\nTotal price: ${total_price:.2f}"

# NestedBox attempts to handle both SimpleBox and MobilePhoneBox, but this adds complexity
class NestedBox:
    def __init__(self):
        self._contents = []

    def add_box(self, box):
        if isinstance(box, (SimpleBox, MobilePhoneBox)):
            self._contents.append(box)
        else:
            raise TypeError("NestedBox can only contain SimpleBox or MobilePhoneBox instances")

    def calculate_total_price(self) -> float:
        return sum(box.calculate_total_price() for box in self._contents)

    def display(self):
        nested_details = "\n".join(f"{box.display()}" for box in self._contents)
        total_price = self.calculate_total_price()
        return f"NestedBox:\n{nested_details}\nTotal price of all nested boxes: ${total_price:.2f}"

if __name__ == "__main__":
    # Creating simple products
    product1 = SimpleProduct("Product 1", 10.0)
    product2 = SimpleProduct("Product 2", 15.0)
    mobile_product = MobilePhoneProduct("Mobile Phone 1", 200.0, 12)

    # Creating SimpleBox with SimpleProducts
    simple_box = SimpleBox()
    simple_box.add_product(product1)
    simple_box.add_product(product2)

    # Creating MobilePhoneBox with a MobilePhoneProduct
    mobile_phone_box = MobilePhoneBox()
    mobile_phone_box.add_product(mobile_product)

    # Creating a NestedBox to hold SimpleBox and MobilePhoneBox
    nested_box = NestedBox()
    nested_box.add_box(simple_box)
    nested_box.add_box(mobile_phone_box)

    # Display details of the nested structure
    print(nested_box.display())