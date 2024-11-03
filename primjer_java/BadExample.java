package primjer_java;
import java.util.ArrayList;
import java.util.List;

// Klasa za jednostavni proizvod
class SimpleProduct {
    private String title;
    private double price;

    public SimpleProduct(String title, double price) {
        this.title = title;
        this.price = price;
    }

    public double calculatePrice() {
        return price;
    }

    public String getTitle() {
        return title;
    }
}

// Klasa za mobilne uređaje s dodatnim atributom warranty
// class MobilePhoneProduct {
//     private String title;
//     private double price;
//     private int warranty;

//     public MobilePhoneProduct(String title, double price, int warranty) {
//         this.title = title;
//         this.price = price;
//         this.warranty = warranty;
//     }

//     public double calculatePrice() {
//         return price;
//     }

//     public String getTitle() {
//         return title;
//     }
// }

// Klasa SimpleBox koja može pohraniti samo SimpleProduct objekte
class SimpleBox {
    private List<SimpleProduct> products = new ArrayList<>();

    public void addProduct(SimpleProduct product) {
        products.add(product);
    }

    public double calculateTotalPrice() {
        double totalPrice = 0;
        for (SimpleProduct product : products) {
            totalPrice += product.calculatePrice();
        }
        return totalPrice;
    }

    public void displayProducts() {
        System.out.println("Proizvodi u kutiji:");
        for (SimpleProduct product : products) {
            System.out.printf("- %s: $%.2f%n", product.getTitle(), product.calculatePrice());
        }
        System.out.printf("Ukupna cijena kutije: $%.2f%n", calculateTotalPrice());
    }
}

 class Main {
    public static void main(String[] args) {
        // Stvaranje proizvoda
        SimpleProduct product1 = new SimpleProduct("Proizvod 1", 10.0);
        SimpleProduct product2 = new SimpleProduct("Proizvod 2", 15.0);
        SimpleProduct product3 = new SimpleProduct("Proizvod 3", 20.0);
       // MobilePhoneProduct productMobile1 = new MobilePhoneProduct("Mobile1", 3000, 12);

        // Stvaranje SimpleBox i dodavanje SimpleProduct objekata
        SimpleBox box = new SimpleBox();
        box.addProduct(product1);
        box.addProduct(product2);
        box.addProduct(product3);
        /* ovdje će se raspast kod  !!!!!!!!!!!!!!!!!!!!!!!!*/
        //box.addProduct(productMobile1);
        

        // Ovo će uzrokovati grešku, jer MobilePhoneProduct nije kompatibilan sa SimpleBox
        // MobilePhoneProduct phone = new MobilePhoneProduct("Mobilni Telefon", 500, 12);
        // box.addProduct(phone);  // -> Ovo neće raditi, jer MobilePhoneProduct nije SimpleProduct

        // Ispis proizvoda i ukupne cijene
        box.displayProducts();
    }
}