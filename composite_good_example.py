# component abstract class
class Box:    
    def __init__(self):
        pass
    # operation function from diagram, available in all implementations
    def calculate_price(self) -> float:
        raise NotImplementedError("Subclasses should implement this method.")


class Product(Box):
    def __init__(self, title: str, price: float):
        self._title = title
        self._price = price

# operation function from diagram, available in all implementations
    def calculate_price(self) -> float:
        return self._price


class CompositeBox(Box):
    def __init__(self, *boxes: Box):
        self._children = list(boxes)

# operation function from diagram, available in all implementations
    def calculate_price(self) -> float:  
        return sum(child.calculate_price() for child in self._children)                 


    def __str__(self):
        product_details = "\n".join(f"- {child._title}: ${child.calculate_price():.2f}" for child in self._children)
        total_price = self.calculate_price()
        return f"Proizvodi u composite box:\n{product_details}\n Total price of the box: ${total_price:.2f}"
    

if __name__ == "__main__":
    products = [
        Product("Product 1", 10.0),
        Product("Product 2", 15.0),
        Product("Product 3", 20.0)
    ]

    composite_box = CompositeBox(*products)
    print(composite_box)