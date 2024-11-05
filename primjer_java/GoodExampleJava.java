package primjer_java;
import java.util.ArrayList;
import java.util.List;

// Apstraktna klasa Box kao zajednički interfejs za sve komponente
abstract class Box {
    public abstract double calculatePrice();

    // Metoda add podiže UnsupportedOperationException osim u CompositeBox klasi
    public void add(Box box) {
        throw new UnsupportedOperationException("Cannot add to a leaf component.");
    }

    // Metoda remove podiže UnsupportedOperationException osim u CompositeBox klasi
    public void remove(Box box) {
        throw new UnsupportedOperationException("Cannot remove from a leaf component.");
    }
}

// Leaf klasa za pojedinačne proizvode koji nemaju djece
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
        return String.format("%s: $%.2f", title, price);
    }
}

// Još jedan Leaf primjer
class MobileProduct extends Box {
    private String title;
    private double price;
    private int warranty;

    public MobileProduct(String title, double price, int warranty) {
        this.title = title;
        this.price = price;
        this.warranty = warranty;
    }

    @Override
    public double calculatePrice() {
        return price;
    }

    @Override
    public String toString() {
        return String.format("%s (Warranty: %d months): $%.2f", title, warranty, price);
    }
}

// Composite klasa koja može sadržavati druge Box objekte
class CompositeBox extends Box {
    private List<Box> children;

    public CompositeBox() {
        this.children = new ArrayList<>();
    }

    // Implementacija add metode samo za CompositeBox
    @Override
    public void add(Box box) {
        children.add(box);
    }

    // Implementacija remove metode samo za CompositeBox
    @Override
    public void remove(Box box) {
        children.remove(box);
    }

    @Override
    public double calculatePrice() {
        // Računa cijenu zbrajanjem cijena svih djece
        return children.stream().mapToDouble(Box::calculatePrice).sum();
    }

    @Override
    public String toString() {
        StringBuilder productDetails = new StringBuilder("Products in composite box:\n");
        for (Box child : children) {
            productDetails.append(child).append("\n");
        }
        double totalPrice = calculatePrice();
        return String.format("%sTotal price of the box: $%.2f", productDetails.toString(), totalPrice);
    }
}

// Primjer korištenja
 class Main {
    public static void main(String[] args) {
        // Kreiranje pojedinačnih proizvoda (Leaf komponente)
        Product product1 = new Product("Product 1", 21.00);
        Product product2 = new Product("Product 2", 24.00);
        Product product3 = new Product("Product 3", 29.00);
        MobileProduct mobileProduct = new MobileProduct("Mobile Product", 2340.0, 12);

        // Kreiranje kompozitne strukture
        CompositeBox innerBox = new CompositeBox();
        innerBox.add(product1);
        innerBox.add(product2);
        innerBox.add(mobileProduct);

        // Kreiranje još jednog kompozita
        CompositeBox outerBox = new CompositeBox();
        outerBox.add(innerBox);  // Dodajemo innerBox kao deo outerBox
        outerBox.add(product3);

        // Ispis strukture i ukupne cene
        System.out.println("Outer box price structure:");
        System.out.println(outerBox);

        // Uklanjanje proizvoda iz innerBox
        innerBox.remove(product1);
        System.out.println("\nAfter removing Product 1 from inner box:");
        System.out.println(outerBox);

    
    }
}
