#!/usr/bin/env python3

### Author: Ruqayya Nooreen


# This function displays the title
def display_title():
  print("===================================")
  print("   Grocery Shopping List      ")
  print("===================================")


# This function displays the command menu
def display_menu():
  print("""\nCOMMAND MENU
  show - Show all items
  grab - Grab an item
  drop - Drop an item
  exit - Exit program""")


# This function shows the items in the shopping_list
def show(shopping_list):
  for i in range(0,len(shopping_list)):
    print(f"{i+1}. {shopping_list[i]}")
   


# This function adds an item to the shopping_list
def grab_item(shopping_list):
  if len(shopping_list)<4:
    new_item=input("Item Name:")
    shopping_list.append(new_item)
    print(f"{new_item} was added.")
  else:
    print("Your shopping list is full. Remove something first.")


#This function deletes an item from the shopping_list
def drop_item(shopping_list):
  number= int(input("Number:"))
  if number < 1 or number > len(shopping_list):
     print("Invalid item number")
     drop_item(shopping_list)
  else:
     dropped_item=shopping_list.pop(number-1)
     print(f"{dropped_item} was dropped.")



# This function displays the final message
def end_message():
  print("\nBye!")


# Defining the main function
def main():
  display_title()
  shopping_list = ["milk", "bread", "eggs"]
  display_menu()
  response=input("\nCommand: ")

  while response.lower() != "exit":

    if response.lower()=="show":
      show(shopping_list)
    elif response.lower()=="grab":
      grab_item(shopping_list)
    elif response.lower()=="drop":
      drop_item(shopping_list)
    else:
      print("Enter the Right Command")
    response=input("\nCommand: ") 
  

  end_message()


# Calling the main function
if __name__ == "__main__":
  main()
