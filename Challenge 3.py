#Challenge: Grocery list
#Ask the user how many grocery items they want to add.
#Let them enter each item and store them in a list.
#Show the full list back to them.
#Add features:
#Print the list in alphabetical order.
#Show how many items are in the list.
#Ask if they want to remove an item (and if yes, delete it from the list).
#Finally, print the updated list.

# ❌ My Attempt
grocery=int(input("How many groceries do you want to buy?:"))
store=\[]
count=0
while True:
if count>=grocery:
break
item=input("What items did you buy?:")
store.append(item)
count+=1
print(f'Your grocery list:{store}')
print(f'Here is what you bought in alphabetical order:{sorted(store)}')
print("Total item:"+str(grocery))
choice=input("Do you want to delete any item in the list?:").lower()
while choice not in \["yes","no"]:
print("wrong input.pls enter the Yes or NO")
choice = input("Do you want to delete any item in the list?:").lower()
else:
if choice=="yes":
delete =input("what would you like to remove?:").lower()
if delete not in store:
print("Sorry, that item is not on the list")
exit()
store.remove(delete)
print(f'Update list:{store}')
else:
print("good bye")
exit()

# ✅ Corrected Version (after AI Tutor feedback)
# That’s a solid solution!
# print("Total items:", len(store))
#store.append(item.lower()) insted of store.append(item)
Exit after delete:
store.remove(delete)
print(f'Updated list: {store}')
print("Total items now:", len(store))
