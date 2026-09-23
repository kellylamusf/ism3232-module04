# week5_lab.py
# Author: Kelly Lam
# Business Domain: Laptop Purchasing System

product_name = "Laptop"
status = "Pending"
quantity = 3
unit_price = 450.00
is_over_limit = unit_price * quantity > 1000

print(type(product_name), type(quantity), type(unit_price), type(is_over_limit))

subtoatl = unit_price * quantity
tax = subtoatl * 0.07
total = subtoatl + tax
requires_approval = total > 1000

print("=== Purchase Request Summary ===")
print(f"Product: {product_name}")
print(f"Qty: {quantity}")
print(f"Subtotal: ${subtoatl:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Requires Approval: {requires_approval}")

user_qty = int(input("Enter a new quantity: "))
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"Requires Approval: {new_total > 1000}")
