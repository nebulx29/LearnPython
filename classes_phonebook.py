
class Phonebook():
	def __init__(self):
		self.__entries = {}       # attributes starting with "__" are private
	
	def add(self, name, phonenr):
		self.__entries[name] = phonenr
		
	def __hasnr(self, name):      # methods starting with "__" are private
		if name in self.__entries:
			return True
		else:
			return False

	def get(self, name):
		if self.__hasnr(name) == True:
			return self.__entries[name]
		else:
			return None
		
	def __str__(self):            # entspricht java toString()
		return "PhoneBook(" + str(self.__entries) + ")"
	
	def __repr__(self):           # entspricht java toString() wenn ohne print()
		return self.__str__()
			
	def __len__(self):
		return len(self.__entries)

book = Phonebook()
book.add("mike", "+4312341234")
book.add("joe", "+4343124312")
#print(book.get("mike"))

print(book)

print(len(book))

#print(book.__entries.keys())     ## ERROR (field private)
#print(book.__hasnr("mike"))      ## ERROR (method private)
	