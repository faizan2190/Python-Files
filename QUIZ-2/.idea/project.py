cart = {}
detail = 'This Product is from the "The Ocean" Company.'
productDictionary = [['1.Air Condtioner', 80000], ['2.Laptop', 50000], ['3.Mobile', 60000]
    , ['4.Washing Machine', 40000]]
def menu():
    print('1. View Product List\n2. View Cart\n3. Checkout\n4. View Shopping History')

def cart_update(key, value):
    cart.update({key: value})


def details(choice):
    print(detail, f'Price of this Product is: {productDictionary[choice][1]}\n', sep='\n')


def product_list():
    for i in range(len(productDictionary)):
        print(productDictionary[i][0])


def main():
    while True:
    # printing the product list
        menu()
        product_list()

        choice = input('Enter the option number: ')

    # printing the details of the product
        details(choice)

        buy = input('Press b to add the item in your cart\n')
        if buy == 'b' or 'B':
            choice = int(choice)
            cart_update(productDictionary[choice - 1][0], productDictionary[choice - 1][1])
            print("Item has been succesfully added to the cart")



main()
