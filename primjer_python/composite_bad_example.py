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
    
    # Ovaj poziv će izazvati grešku jer SimpleBox ne može primiti MobilePhoneProduct
    # simple_box.add_product(mobile_product)

    # Creating MobilePhoneBox with a MobilePhoneProduct
    mobile_phone_box = MobilePhoneBox()
    mobile_phone_box.add_product(mobile_product)

    # Creating a NestedBox to hold SimpleBox and MobilePhoneBox
    nested_box = NestedBox()
    nested_box.add_box(simple_box)
    nested_box.add_box(mobile_phone_box)

    # Display details of the nested structure
    print(nested_box.display())
