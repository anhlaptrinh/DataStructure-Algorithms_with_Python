# Product management script in Python

# Initialize the product list with 3 sample products
products = [
    {"name": "Product 1", "price": 100, "quantity": 10},
    {"name": "Product 2", "price": 200, "quantity": 5},
    {"name": "Product 3", "price": 300, "quantity": 3}
]

def display_products():
    print("\nCurrent Product List:")
    for index, product in enumerate(products):
        print(f"{index + 1}. Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    products.append({"name": name, "price": price, "quantity": quantity})
    print("Product added successfully!")

def delete_product():
    display_products()
    index = int(input("Enter the product number to delete: ")) - 1
    if 0 <= index < len(products):
        products.pop(index)
        print("Product deleted successfully!")
    else:
        print("Invalid product number!")

def edit_product():
    display_products()
    index = int(input("Enter the product number to edit: ")) - 1
    if 0 <= index < len(products):
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        quantity = int(input("Enter new product quantity: "))
        products[index] = {"name": name, "price": price, "quantity": quantity}
        print("Product updated successfully!")
    else:
        print("Invalid product number!")

def search_product():
    search_name = input("Enter the product name to search: ")
    found_products = [product for product in products if search_name.lower() in product['name'].lower()]
    if found_products:
        print("\nSearch Results:")
        for product in found_products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print("No products found with that name.")

def main():
    while True:
        print("\nProduct Management")
        print("1. View Products")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Edit Product")
        print("5. Search Product")
        print("6. Exit")
        
        try:
            choice = input("Enter your choice: ")
            
            if choice == '1':
                display_products()
            elif choice == '2':
                add_product()
            elif choice == '3':
                delete_product()
            elif choice == '4':
                edit_product()
            elif choice == '5':
                search_product()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
