class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.shopping_cart = []  # Initialize an empty list to store items in the shopping cart
        self.last_transaction_amount = 0  # Keep track of the last transaction amount

    def add_item(self, item, price):
        self.shopping_cart.append({'item': item, 'price': price})
        self.last_transaction_amount = price  # Update the last_transaction_amount

    def apply_discount(self):
        total = sum([item['price'] for item in self.shopping_cart])
        discounted_total = total - (total * self.discount / 100)
        print(discounted_total)
        return discounted_total

    def void_last_transaction(self):
        if self.shopping_cart:  # Check if the shopping cart is not empty
            # Remove the last transaction from the shopping cart
            removed_item = self.shopping_cart.pop()
            self.last_transaction_amount = -removed_item['price']  # Update last_transaction_amount
            print("Last transaction voided.")
        else:
            print("Shopping cart is empty.")

# Example usage:
t = CashRegister(20)  # Set a discount of 20%
t.add_item("Shirt", 25)  # Add an item with a price of $25 to the shopping cart
t.add_item("Pants", 30)  # Add another item with a price of $30 to the shopping cart
print("Total before discount:", sum([item['price'] for item in t.shopping_cart]))
discounted_total = t.apply_discount()
t.void_last_transaction()
print("Total after voiding last transaction:", sum([item['price'] for item in t.shopping_cart]))
