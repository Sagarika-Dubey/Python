# grocery-list program
#take items update list and print the bill at last

budget=int(input("Enter your budget"))
list_product=[]
list_quant=[]
list_price=[]
while True :
    choice=int(input("1)Add an item \n"
          "2)Exit \n"
          "Enter your choice-"))

    if (choice==1 and budget>0):
        product=input("Enter the product name")
        list_product.append(product)
        quant= float(input("Enter the quantity taken"))
        list_quant.append(quant)
        price=float(input("Enter the price of the product per kg"))
        price=price*quant
        list_price.append(price)
        budget=budget-price
        print("\n Amount left=",budget)

        if (price>budget):
            print("Cant buy product")
            continue
    elif(budget<=0):
        print("Out of budget")
    else:
        print("Printing the bill:")
        break
print("Product Name \tQuatity \tPrice")
for i in range(len(list_product)):
    print(list_product[i],list_quant[i],list_price[i])
bill=0
for i in range(len(list_price)):
    bill=bill+list_price[i]

print("Your total bill is:",bill)
print("Thanks for shopping with us❤ \nDo visit the store again:)")
