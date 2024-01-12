#python project of taking order from user and giving bill
def menu():
  print("1. Tea              20Rs \n"
        "2. Coffee           30Rs \n"
        "3. Ice Cream        50Rs \n"
        "4. Burger           150Rs \n"
        "5. Pizza            200Rs \n"
        "6. French Fries     100Rs \n"
        "7. Sandwich         100Rs \n"
        "8. Pasta            150Rs")
  choice = input("Your Order: ")
  return choice


def bill(choice):
  if (choice == "1"):
    bill = 20
  elif (choice == "2"):
    bill = 30
  elif (choice == "3"):
    bill = 50
  elif (choice == "4" or choice == "8"):
    bill = 150
  elif (choice == "5"):
    bill = 200
  elif (choice =="6" or choice=="7"):
    bill = 100
  else:
    bill= 0
  return bill


def discount(bill):
  dis = bill * 0.2
  return dis


#main
name = input("Hey! What's your name? ")
print("Welcome to our resturant", name)
print("\n")
ans = "yes"
while (ans == "yes"):
  order = menu()
  quan = int(input("Quantity: "))
  a = bill(order)
  final = a * quan
  print("Your bill is", final)
  b = discount(final)
  print("As a celebration of new year we are happy to tell that"
        "we are providing some new year discount")
  print("So your final bill is:", final - b, "\n")
  ans = input("Do you want to order again(yes/no)?")
  if(ans=="yes" or ans=="Yes" or ans=="YES"):
    continue
  else:
    print("Thanks for ordering. \nVist Again")
  
  print("\n")
