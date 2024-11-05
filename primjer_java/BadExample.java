// package primjer_java;
// import java.util.ArrayList;
// import java.util.List;

// // Klasa za jednostavni proizvod
// class SimpleProduct {
//     private String title;
//     private double price;

//     public SimpleProduct(String title, double price) {
//         this.title = title;
//         this.price = price;
//     }

//     public double calculatePrice() {
//         return price;
//     }

//     public String getTitle() {
//         return title;
//     }
// }

// // Klasa za mobilne uređaje s dodatnim atributom warranty
// // class MobilePhoneProduct {
// //     private String title;
// //     private double price;
// //     private int warranty;

// //     public MobilePhoneProduct(String title, double price, int warranty) {
// //         this.title = title;
// //         this.price = price;
// //         this.warranty = warranty;
// //     }

// //     public double calculatePrice() {
// //         return price;
// //     }

// //     public String getTitle() {
// //         return title;
// //     }
// // }

// // Klasa SimpleBox koja može pohraniti samo SimpleProduct objekte
// class SimpleBox {
//     private List<SimpleProduct> products = new ArrayList<>();

//     public void addProduct(SimpleProduct product) {
//         products.add(product);
//     }

//     public double calculateTotalPrice() {
//         double totalPrice = 0;
//         for (SimpleProduct product : products) {
//             totalPrice += product.calculatePrice();
//         }
//         return totalPrice;
//     }

//     public void displayProducts() {
//         System.out.println("Proizvodi u kutiji:");
//         for (SimpleProduct product : products) {
//             System.out.printf("- %s: $%.2f%n", product.getTitle(), product.calculatePrice());
//         }
//         System.out.printf("Ukupna cijena kutije: $%.2f%n", calculateTotalPrice());
//     }

//     public static void main(String[] args) {
//         // Stvaranje proizvoda
//         SimpleProduct product1 = new SimpleProduct("Proizvod 1", 10.0);
//         SimpleProduct product2 = new SimpleProduct("Proizvod 2", 15.0);
//         SimpleProduct product3 = new SimpleProduct("Proizvod 3", 20.0);
//        // MobilePhoneProduct productMobile1 = new MobilePhoneProduct("Mobile1", 3000, 12);

//         // Stvaranje SimpleBox i dodavanje SimpleProduct objekata
//         SimpleBox box = new SimpleBox();
//         box.addProduct(product1);
//         box.addProduct(product2);
//         box.addProduct(product3);
//         /* ovdje će se raspast kod  !!!!!!!!!!!!!!!!!!!!!!!!*/
//         //box.addProduct(productMobile1);
        

//         // Ovo će uzrokovati grešku, jer MobilePhoneProduct nije kompatibilan sa SimpleBox
//         // MobilePhoneProduct phone = new MobilePhoneProduct("Mobilni Telefon", 500, 12);
//         // box.addProduct(phone);  // -> Ovo neće raditi, jer MobilePhoneProduct nije SimpleProduct

//         // Ispis proizvoda i ukupne cijene
//         box.displayProducts();
//     }
// }
package primjer_java;
import java.util.ArrayList;
import java.util.List;

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

    public String display() {
        return String.format("%s: $%.2f", title, price);
    }
}

class MobilePhoneProduct {
    private String title;
    private double price;
    private int warranty;

    public MobilePhoneProduct(String title, double price, int warranty) {
        this.title = title;
        this.price = price;
        this.warranty = warranty;
    }

    public double calculatePrice() {
        return price;
    }

    public String display() {
        return String.format("%s: $%.2f (Warranty: %d months)", title, price, warranty);
    }
}

class SimpleBox {
    private List<SimpleProduct> products;

    public SimpleBox() {
        this.products = new ArrayList<>();
    }

    public void addProduct(SimpleProduct product) {
        products.add(product);
    }

    public double calculateTotalPrice() {
        return products.stream().mapToDouble(SimpleProduct::calculatePrice).sum();
    }

    public String display() {
        StringBuilder productDetails = new StringBuilder("SimpleBox:\n");
        products.forEach(product -> productDetails.append("- ").append(product.display()).append("\n"));
        productDetails.append("Total price: $").append(String.format("%.2f", calculateTotalPrice()));
        return productDetails.toString();
    }
}

class MobilePhoneBox {
    private List<MobilePhoneProduct> products;

    public MobilePhoneBox() {
        this.products = new ArrayList<>();
    }

    public void addProduct(MobilePhoneProduct product) {
        products.add(product);
    }

    public double calculateTotalPrice() {
        return products.stream().mapToDouble(MobilePhoneProduct::calculatePrice).sum();
    }

    public String display() {
        StringBuilder productDetails = new StringBuilder("MobilePhoneBox:\n");
        products.forEach(product -> productDetails.append("- ").append(product.display()).append("\n"));
        productDetails.append("Total price: $").append(String.format("%.2f", calculateTotalPrice()));
        return productDetails.toString();
    }
}

class NestedBox {
    private List<Object> contents;

    public NestedBox() {
        this.contents = new ArrayList<>();
    }

    public void addBox(Object box) {
        if (box instanceof SimpleBox || box instanceof MobilePhoneBox) {
            contents.add(box);
        } else {
            throw new IllegalArgumentException("NestedBox can only contain SimpleBox or MobilePhoneBox instances");
        }
    }

    public double calculateTotalPrice() {
        return contents.stream()
                .filter(box -> box instanceof SimpleBox)
                .mapToDouble(box -> ((SimpleBox) box).calculateTotalPrice())
                .sum() +
               contents.stream()
                .filter(box -> box instanceof MobilePhoneBox)
                .mapToDouble(box -> ((MobilePhoneBox) box).calculateTotalPrice())
                .sum();
    }

    public String display() {
        StringBuilder nestedDetails = new StringBuilder("NestedBox:\n");
        contents.forEach(box -> {
            if (box instanceof SimpleBox) {
                nestedDetails.append(((SimpleBox) box).display()).append("\n");
            } else if (box instanceof MobilePhoneBox) {
                nestedDetails.append(((MobilePhoneBox) box).display()).append("\n");
            }
        });
        nestedDetails.append("Total price of all nested boxes: $").append(String.format("%.2f", calculateTotalPrice()));
        return nestedDetails.toString();
    }
}

 class Main {
    public static void main(String[] args) {
        // Creating simple products
        SimpleProduct product1 = new SimpleProduct("Product 1", 10.0);
        SimpleProduct product2 = new SimpleProduct("Product 2", 15.0);
        MobilePhoneProduct mobileProduct = new MobilePhoneProduct("Mobile Phone 1", 200.0, 12);

        // Creating SimpleBox with SimpleProducts
        SimpleBox simpleBox = new SimpleBox();
        simpleBox.addProduct(product1);
        simpleBox.addProduct(product2);

        // Ovaj poziv će izazvati grešku jer SimpleBox ne može primiti MobilePhoneProduct
        // simpleBox.addProduct(mobileProduct); // Uncomment to see the error

        // Creating MobilePhoneBox with a MobilePhoneProduct
        MobilePhoneBox mobilePhoneBox = new MobilePhoneBox();
        mobilePhoneBox.addProduct(mobileProduct);

        // Creating a NestedBox to hold SimpleBox and MobilePhoneBox
        NestedBox nestedBox = new NestedBox();
        nestedBox.addBox(simpleBox);
        nestedBox.addBox(mobilePhoneBox);

        // Display details of the nested structure
        System.out.println(nestedBox.display());
    }
}
