# Supermarket cashier

# Accepting the product 

def product_details(prod_data,prod_name,prod_qty):
    prod_data.update({prod_name:prod_qty})
    return prod_data

prod_data  = {} 
option  = True
while(option):
    prod_name = input("Enter the product name: ")
    prod_qty = int(input("Enter the quantity: "))
    prod_details = product_details(prod_data,prod_name,prod_qty) 
    Add_product = input("Add product(Y/N): ")
    if(Add_product == 'N'):
        break
    elif(Add_product != 'A'):
        print("Enter the correct option")

print("Product brought:")
print(prod_details)