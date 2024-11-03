#u ovom primjeru je ista struktura Product, ali bez implementacije Box interfejsa
class Product:  
    def __init__(self, title: str, price: float):
        self._title = title
        self._price = price

    def calculate_price(self) -> float:
        return self._price

# kada bih htio dodati kutije s drugim vrstama proizvoda, na primjer bananama, ili tenisicama, morao bih stvoriti novu klasu sličnu SimpleBox 

class SimpleBox:
    def __init__(self):
        self._products = []  # Lista za pohranu proizvoda u tijelu konstruktora

    def add_product(self, product: Product):
        self._products.append(product)

    def calculate_total_price(self) -> float:
        total_price = 0
        for product in self._products:
            total_price += product.calculate_price()
        return total_price

    def display_products(self):
        print("Proizvodi u kutiji:")
        for product in self._products:
            print(f"- {product._title}: ${product.calculate_price():.2f}")
        print(f"Ukupna cijena kutije: ${self.calculate_total_price():.2f}")

"""class MobilePhoneBox:
    def __init__(self):
        self._products = []  # Lista za pohranu proizvoda

    def add_product(self, product: Product):
        self._products.append(product)

    def calculate_total_price(self) -> float:
        total_price = 0
        for product in self._products:
            total_price += product.calculate_price()
        return total_price

    def display_products(self):
        print("Proizvodi u kutiji:")
        for product in self._products:
            print(f"- {product._title}: ${product.calculate_price():.2f}")
        print(f"Ukupna cijena kutije: ${self.calculate_total_price():.2f}")
"""
if __name__ == "__main__":
    # Stvaranje proizvoda
    product1 = Product("Proizvod 1", 10.0)
    product2 = Product("Proizvod 2", 15.0)
    product3 = Product("Proizvod 3", 20.0)

    # Stvaranje jednostavne kutije i dodavanje proizvoda
    """pa kad bih htio dodati nove mobitele u kutiju bih trebao stvoriti posebno instancu MobilePhone kutije...
    Ako želim da SimpleBox može raditi s MobilePhoneProduct, možda ću morati dodati dodatnu logiku unutar SimpleBox
      da bih ispravno obradio novu klasu."""
    simple_box = SimpleBox()
    simple_box.add_product(product1)
    simple_box.add_product(product2)
    simple_box.add_product(product3)

    # Ispis proizvoda i ukupne cijene
    simple_box.display_products()