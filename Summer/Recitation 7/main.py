from classes import Person

def main():
	amir = Person('Amir', 42, 'happy', True)

	# The right way
	amir.description()
	amir.set_age(567)
	amir.set_age(28)
	amir.description()
	print(amir.get_emotion())
	amir.set_emotion('tired')
	print(amir.get_emotion())
	amir.description()
main()
