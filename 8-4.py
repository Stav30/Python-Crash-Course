def make_shirt(size = 'large', message = 'I love Python'):
	""" Display size and message"""
	if size in ['medium', 'large'] :
		print(f"\n the shirt size is {size}")
		print(f"\n the message is {message}")
	else:
		print(f"\nthe shirt size is {size}")
		print(f"\nthe message is shirt is NOT a medium or large")

make_shirt(size='small')
