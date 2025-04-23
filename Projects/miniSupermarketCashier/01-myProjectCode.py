# Mini Supermarket cashier application
# Membership discount will be given if billamount exceeds Rs.500

# Functions
def billAmount(product,prod_details):
    billAmount = 0
    for key,value in product.items():
        billAmount += (prod_details[key])*value
    return billAmount

def billDiscount(bill,mem_discount):
    discount = 0
    if bill>500:
        print('Congrats, You have purchased for Rs.',bill)
        print("You are selected for membership discount")
        mem_access = input("Membership available?(y/n):")
        if('n' in  mem_access or 'no' in mem_access):
            return discount
        else:
            membership = (input("Enter your membership (Gold/Silver/Bronze):")).lower()
            for key,value in mem_discount.items():
                if membership == key:
                    discount = value*0.01*bill
                    print("")
                    print(str(value)+"% discount for",membership.capitalize(),"membership")
                    return discount
            else: 
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
    input_item = True
    while(input_item):
        prod_input = (input("Add product:")).lower()
        for i in prod_details:
            if i == prod_input:
                input_item = False
                break
        else:
            print("Select the right product")
    
    while(True):
        try:
            qty_input = int(input("Add quantity:"))
        except Exception:
            print("Its not a number")
        else:
            break
    product.update({prod_input:qty_input})
    contd = (input("continue? (y/n):")).lower()
    if (('n' in contd) or ('no' in contd)):
        option = False


# Calculating total
bill = billAmount(product,prod_details)

# Adding discount
discount = billDiscount(bill,mem_discount)
print("Discount: Rs.",discount)
print("")

# Making final bill
final_bill = bill-discount
print("Bill details:")
print("------------")
for key,value in product.items():
        print(key.capitalize(),"= Rs.",prod_details[key]," X ",value," = ",(prod_details[key])*value)
print("Total Bill amount:Rs.",bill)
print("Less: discount Rs.",discount)
print("Net Bill amount = Rs.",final_bill)
print("Thanks for shopping!")