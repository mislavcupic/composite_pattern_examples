from abc import ABC, abstractmethod

# Apstraktna klasa Box kao zajednički interfejs za sve komponente
class Box(ABC):
    @abstractmethod
    def calculate_price(self) -> float:
        """Metoda za izračun cijene. Implementira je svaka podklasa."""
        pass

    # Metoda add podiže NotImplementedError osim u CompositeBox klasi
    def add(self, box: 'Box'):
        raise NotImplementedError("Cannot add to a leaf component.")

    # Metoda remove podiže NotImplementedError osim u CompositeBox klasi
    def remove(self, box: 'Box'):
        raise NotImplementedError("Cannot remove from a leaf component.")


# Leaf klasa za pojedinačne proizvode koji nemaju djece
class Product(Box):
    def __init__(self, title: str, price: float):
        self._title = title
        self._price = price

    def calculate_price(self) -> float:
        return self._price

    def __str__(self):
        return f"{self._title}: ${self._price:.2f}"


# Još jedan Leaf primjer
class MobileProduct(Box):
    def __init__(self, title: str, price: float, warranty: int):
        self._title = title
        self._price = price
        self._warranty = warranty

    def calculate_price(self) -> float:
        return self._price

    def __str__(self):
        return f"{self._title} (Warranty: {self._warranty} months): ${self._price:.2f}"


# Composite klasa koja može sadržavati druge Box objekte
class CompositeBox(Box):
    def __init__(self):
        self._children = []

    # Implementacija add metode samo za CompositeBox
    def add(self, box: Box):
        self._children.append(box)

    # Implementacija remove metode samo za CompositeBox
    def remove(self, box: Box):
        self._children.remove(box)

    def calculate_price(self) -> float:
        # Računa cijenu zbrajanjem cijena svih djece
        return sum(child.calculate_price() for child in self._children)

    def __str__(self):
        product_details = "\n".join(str(child) for child in self._children)
        total_price = self.calculate_price()
        return f"Products in composite box:\n{product_details}\nTotal price of the box: ${total_price:.2f}"


# Primjer korištenja
if __name__ == "__main__":
    # Kreiranje pojedinačnih proizvoda (Leaf komponente)
    product1 = Product("Product 1", 21.00)
    product2 = Product("Product 2", 24.00)
    product3 = Product("Product 3", 29.00)
    mobile_product = MobileProduct("Mobile Product", 2340.0, 12)
    

    # Kreiranje kompozitne strukture
    inner_box = CompositeBox()
    inner_box.add(product1)
    inner_box.add(product2)
    inner_box.add(mobile_product)

    # Kreiranje još jednog kompozita
    outer_box = CompositeBox()
    outer_box.add(inner_box)  # Dodajemo inner_box kao dio outer_box
    outer_box.add(product3)

    # Ispis strukture i ukupne cijene
    print("Outer box price structure:")
    print(outer_box)

    # Uklanjanje proizvoda iz inner_box
    inner_box.remove(product1)
    print("\nAfter removing Product 1 from inner box:")
    print(outer_box)

