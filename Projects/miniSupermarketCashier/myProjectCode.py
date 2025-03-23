# Supermarket cashier
# Membership discount will be given if billamount exceeds Rs.500

# Functions
def billAmount(product,prod_details):
    billAmount = 0
    print("Bill details:")
    print("------------")
    for key,value in product.items():
        print(key.capitalize(),"= Rs.",prod_details[key]," X ",value," = ",(prod_details[key])*value)
        billAmount += (prod_details[key])*value
    return billAmount

def billDiscount(bill,mem_discount):
    discount = 0
    if bill>500:
        print("You are selected for membership discount")
        mem_access = input("Membership available?(y/n):")
        if('n' in  mem_access or 'no' in mem_access):
            return discount
        else:
            membership = (input("Enter your membership (Gold/Silver/Bronze):")).lower()
            for key,value in mem_discount.items():
                if membership == key:
                    discount = value*0.01*bill
                return discount
    else:
        return discount

# Main Program
print("Welcome to Vilvam supermarket")
print("-----------------------------")
print("Our Products:")
print(""" 
        Biscuit: Rs.25,
        Chicken: Rs.250 (per kg),
        Egg: Rs.8,
        Fish: Rs.100 (per kg),
        Coke: Rs.50,
        Bread: Rs.20,
        Apple: Rs.100 (per kg),
        Onion: Rs.45 (per kg)
""")
prod_details={
    'biscuit':25,
    'chicken':250,
    'egg':8,
    'fish':100,
    'coke':50,
    'bread':20,
    'apple':100,
    'onion':45
}

mem_discount={
        'gold':20,
        'silver':10,
        'bronze':5
    }

# Product updation
product = {}
option = True
while(option):
    prod_input = (input("Add product:")).lower()
    qty_input = int(input("Add quantity:"))
    product.update({prod_input:qty_input})
    contd = (input("continue? (y/n):")).lower()
    if (('n' in contd) or ('no' in contd)):
        option = False
print(product)

# Calculating total
bill = billAmount(product,prod_details)
print("Bill amount:",bill)

# Adding discount
discount = billDiscount(bill,mem_discount)
print("Discount: Rs.",discount)