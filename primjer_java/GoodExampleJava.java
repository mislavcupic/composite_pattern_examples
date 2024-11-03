package primjer_java;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// Component abstract class
abstract class Box {
    // Method to be implemented by all subclasses
    public abstract double calculatePrice();
}

// Leaf class representing individual products
class Product extends Box {
    private String title;
    private double price;

    public Product(String title, double price) {
        this.title = title;
        this.price = price;
    }

    @Override
    public double calculatePrice() {
        return price;
    }

    @Override
    public String toString() {
        return "- " + title + ": $" + String.format("%.2f", price);
    }
}

// Composite class to hold multiple boxes or products
class CompositeBox extends Box {
    private List<Box> children = new ArrayList<>();

    public CompositeBox(Box... boxes) {
        children.addAll(Arrays.asList(boxes));
    }

    @Override
    public double calculatePrice() {
        double totalPrice = 0;
        for (Box child : children) {
            totalPrice += child.calculatePrice();
        }
        return totalPrice;
    }

    @Override
    public String toString() {
        StringBuilder productDetails = new StringBuilder("Proizvodi u composite box:\n");
        for (Box child : children) {
            productDetails.append(child.toString()).append("\n");
        }
        productDetails.append("Total price of the box: $").append(String.format("%.2f", calculatePrice()));
        return productDetails.toString();
    }
}

 class Main {
    public static void main(String[] args) {
        // Create individual products
        Product product1 = new Product("Product 1", 10.0);
        Product product2 = new Product("Product 2", 15.0);
        Product product3 = new Product("Product 3", 20.0);

        // Create a composite box with products
        CompositeBox compositeBox = new CompositeBox(product1, product2, product3);

        // Print the details of the composite box
        System.out.println(compositeBox);
    }
}
