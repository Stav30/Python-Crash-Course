# More guest
dinner_guests = ['Gauss', 'Archimedes','Socrates']
print(f"{dinner_guests[0]} is one of my dinner guests")
print(f"{dinner_guests[1]} is one of my dinner guests")
print(f"{dinner_guests[2]} is one of my dinner guests")
print("\n")
guest_cancelled = dinner_guests.pop(1)
print(f"{guest_cancelled} is not able to make the dinner ")
dinner_guests.insert(1, 'Descartes') 
print(dinner_guests)
print(f"\n Hello {dinner_guests[0]}, {dinner_guests[1]} and {dinner_guests[2]}. A larger table has become available and we shall have 3 additional guests")
dinner_guests.insert(0, 'Plato')
dinner_guests.insert(3, 'Nietzsche')
dinner_guests.append('Plutarch')
print(dinner_guests)
for guest in dinner_guests :
	print(f"{guest} you are invited to my dinner party")
