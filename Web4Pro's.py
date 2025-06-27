def web4pro_cart():
    cart = {}
    store_name = "Web4Pro's"
    store_email = "ntombifuthimashinini4@gmail.com"
    
    print(f"\n{'='*50}")
    print(f"WELCOME TO {store_name.upper()} STORE")
    print(f"Contact: {store_email}")
    print(f"{'='*50}\n")
    print("Enter your items below. Type 'checkout' when done.\n")
    
    item_count = 0
    while True:
        item_count += 1
        product = input(f"Item #{item_count} - Product name: ").strip()
        
        if product.lower() == 'checkout':
            if not cart:
                print("\nYour cart is empty. Thank you for visiting!")
                return
            break
            
        while True:
            price_input = input(f"Price for {product}: R").strip()
            try:
                price = float(price_input)
                if price <= 0:
                    print("Price must be positive. Please try again.")
                    continue
                cart[product] = price
                print(f"✓ Added {product} for R{price:.2f}\n")
                break
            except ValueError:
                print("Invalid price. Please enter a valid number (e.g. 12.99)")
    
    total = sum(cart.values())
    
    print("\n" + "=" * 50)
    print(f"{'WEB4PRO\'S RECEIPT':^50}")
    print(f"{'='*50}")
    print(f"{'Item':<30}{'Price':>20}")
    print(f"{'-'*50}")
    for product, price in cart.items():
        print(f"{product[:28]:<30}R{price:>19.2f}")
    print(f"{'-'*50}")
    print(f"{'TOTAL:':<30}R{total:>19.2f}")
    print(f"{'='*50}")
    print(f"Thank you for shopping at {store_name}!")
    print(f"For questions, email: {store_email}")
    print(f"{'='*50}")

if __name__ == "__main__":
    web4pro_cart()