#Question 1


def rev(s, i):

  temp = ""

  if i == 0:
    print("")

  else:
    for ch in s:
      temp = ch + temp

    print(temp * i)


#############################################

#Question 2:


def upper_first(my_str):

  print("original string: ", my_str)

  lower = []
  upper = []

  for ch in my_str:
    if ch.islower():
      lower.append(ch)

    else:
      upper.append(ch)

  sorted_str = ''.join(upper + lower)
  print('result:', sorted_str)


#############################################

#Question 3:


def reordered(str1, str2):

  x = sorted(str1)
  y = sorted(str2)

  if (x == y):
    print('True')
  else:
    print('false')


##############################################

#Question 4:


def min_max(my_list):

  max = my_list[0]
  min = my_list[0]

  for i in range(1, len(my_list)):
    if (my_list[i] > max):
      max = my_list[i]

    elif (my_list[i] < min):
      min = my_list[i]

  print("max:", max)
  print("max index:", my_list.index(max))
  print("min:", min)
  print("min index:", my_list.index(min))


##################################################

#Question 5:


def countdigit(n):

  if n // 10 == 0:
    return 1

  return 1 + countdigit(n // 10)

######################################################

def list_jumps(jumps):
  index = 0
  list_lengh = len(jumps) - 1
  list_of_indices = [0]

  while index >= 0 and index <= list_lengh:
    index = index + jumps[index]

    for i in list_of_indices:
      if index == i:
        print("Cycle!")
        break
        break
      else:
        list_of_indices.append(index)
    break

  print("Out of Boundaries")

######################################################

#POS for aamo el dekanje


def POS():

  new = int(
    input("Do you want to start a new receipt?:\n1 for Yes\n2 for No\n\n"))

  if new == 1:
    start = True
  else:
    start = False

  if (start == True):
    receipt = []

    #Let's build the barcodes database
    #Each item's barcode will be associated with its corresponding name and price

    items_price = {
      1234: 5,
      1122: 4,
      1313: 3,
      3121: 7,
      4123: 3,
      2132: 2,
      4321: 1,
      9876: 6,
      5678: 4,
      4040: 5,
      5656: 5,
      9999: 1,
      5555: 4,
      3030: 6,
      1919: 1,
      6789: 3,
      3333: 5,
      7777: 2,
      6565: 2,
      1414: 10,
      5050: 9,
      5151: 6
    }

    items_name = {
      1234: "cake",
      1122: "Milk",
      1313: "Battery",
      3121: "Oil",
      4123: "Tissues",
      2132: "Chocolate Bar",
      4321: "Biscuit",
      9876: "Tooth Paste",
      5678: "Detergent",
      4040: "Coffee",
      5656: "Cereal",
      9999: "Tea",
      5555: "Rice",
      3030: "Shampoo",
      1919: "Bread",
      6789: "Beans",
      3333: "Chocolate Spread",
      7777: "Chips",
      6565: "Soap",
      1414: "Laundry Detergent",
      5050: "Vegetables",
      5151: "Diapers"
    }

    while start == True:
      barcode = int(input("Item Barcode:  "))
      qty = int(input("Quantity Purchased:  "))
      new_item = [
        barcode, items_name[barcode], qty, items_price[barcode],
        qty * items_price[barcode]
      ]
      receipt.append(new_item)
      print(receipt)
      new = int(
        input("\n\nAny other item to the list?:\n1 for Yes\n2 for No\n\n"))
      if new == 1:
        start = True
      else:
        start = False

  #Calculating the Grand Total
    total_price = 0
    for i in range(len(receipt)):
      total_price = total_price + receipt[i][4]

  #Printing the Final Receipt

    print("Thank you for visiting 3ammo El Dekanje")
    print("Kindly check the Receipt Details")

    for i in range(len(receipt)):
      print(receipt[i][1], "  unit Price: ", receipt[i][3], "  Quantity:  ",
            receipt[i][2], "  Total Price:  ", receipt[i][4])

    print("\n\nGrand Total:  ", total_price)


##########################################################

#Calling the Functions!



rev("Beirut", 7)
upper_first("GoodMorning")
reordered("beirut", "ietbur")
min_max([-1, 3, 2, 10, -4, 5])
countdigit(7586597609)
list_jumps([3, 6, -2, 1, -3, -1, 2, -1, 2, 6, -7])
list_jumps([1, 2, -10, -1, 7, 3, 2])
POS()


