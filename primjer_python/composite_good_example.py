# component abstract class
class Box:    
    def __init__(self):
        pass
    # operation function from diagram, available in all implementations
    def calculate_price(self) -> float:
        raise NotImplementedError("Subclasses should implement this method.")

#i example with different type of product
class MobileProduct(Box):
    def __init__(self, title: str, price: float, warranty: int):
        self._title = title
        self._price = price
        self.warranty = warranty

# operation function from diagram, available in all implementations
    def calculate_price(self) -> float:
        return self._price

class Product(Box):
    def __init__(self, title: str, price: float):
        self._title = title
        self._price = price

# operation function from diagram, available in all implementations
    def calculate_price(self) -> float:
        return self._price

#unlike SimpleBox, MobileBox, NestedBox, CompositeBox doesn't care what type of Box is added
class CompositeBox(Box):
    def __init__(self, *boxes: Box):
        self._children = list(boxes)

# operation function from diagram, available in all implementations
    def calculate_price(self) -> float:  
        return sum(child.calculate_price() for child in self._children)                 


    def __str__(self):
        product_details = "\n".join(
            f"- {child._title}: ${child.calculate_price():.2f}" if isinstance(child, Product) 
            else f"- Nested box total: ${child.calculate_price():.2f}"
            for child in self._children
        )
        total_price = self.calculate_price()
        return f"Products in composite box:\n{product_details}\nTotal price of the box: ${total_price:.2f}"

if __name__ == "__main__":
    #stvaranje pojedinačnih proizvoda i stavljanje u kutiju na jedan način
    products = [
        Product("Product 1", 10.0),
        Product("Product 2", 15.0),
        Product("Product 3", 20.0),
        #MobileProduct("Mobile 1",200.0, 12)
    ]

    composite_box = CompositeBox(*products)
    print(composite_box)

    # but still, CompositeBox can take order its boxes and products in different ways
    product1 = Product("Product 1",21.00)
    product2 = Product("Product 2",24.00)
    product3 = Product("Product 3",29.00)
    product4 = MobileProduct("Mobile 4",2340.0,12)
    # in composite, nesting is solved in one line of code
    inner_box = CompositeBox(product1, product2, product4)
    
    # Create an outer box containing products and the inner box
    outer_box = CompositeBox(inner_box, product3)

    # Print out the details of the outer box
    print("Outer box price: ",outer_box)