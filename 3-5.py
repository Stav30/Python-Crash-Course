# Changing Guest List
dinner_guests = ['Gauss', 'Archimedes','Socrates']
print(f"{dinner_guests[0]} is one of my dinner guests")
print(f"{dinner_guests[1]} is one of my dinner guests")
print(f"{dinner_guests[2]} is one of my dinner guests")
print("\n")
guest_cancelled = dinner_guests.pop(1)
print(f"{guest_cancelled} is not able to make the dinner ")
dinner_guests.insert(1, 'Descartes') 
print(dinner_guests)
