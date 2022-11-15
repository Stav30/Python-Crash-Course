#4-13
menu = ('steak', 'pasta', 'chicken', 'rice', 'vegetables')
for item in menu:
	print("The items on the menu include: ")
	print(item.title())
#reassign the variable menu with 2 different food items
menu = ('bacon', 'pancakes', 'chicken', 'rice', 'vegetables')


print("\n --------")
for item in menu:
	print("The items on the revised menu include: ")
	print(item.title())
