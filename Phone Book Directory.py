class PhoneBook: #represents each entry in the phone directory
    phone_directory = [] #stores contact information

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        PhoneBook.phone_directory.append(self) #add the information of an object/contact to list

    def show_contact(self): #shows only the information of the object we are using
        return f"Name: {self.name}, Phone number: {self.phone_number}"

    @classmethod
    def show_all_contact(cls): #shows all the contact information
        print("Showing all the contacts in the phone directory =>")
        if len(cls.phone_directory) == 0:
            print("No contacts found!")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name): #searches a particular contact
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return f"{search_name}'s Phone Number: {contact.phone_number}"
        return f"No contacts found for {search_name}!"

    @staticmethod
    def valid_phone_number(number):
        if len(number) == 10 and number.isdigit():
            return True
        else:
            return False


no_contacts = int(input("Enter number of contacts you want to add: "))

for i in range(no_contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    if PhoneBook.valid_phone_number(phone_number):
        PhoneBook(name, phone_number)
    else:
        print(f"Invalid phone number for {name}!")

'''
p1 = PhoneBook("John", "9852134765")
p2 = PhoneBook("Mark", "6382145934")
'''

#printing the object in phone_directory
print(PhoneBook.phone_directory)
print("==========================")

'''
#printing the contact of particular object
print(p1.show_contact())
print(p2.show_contact())
print("==========================")
'''

#printing all the contact information
PhoneBook.show_all_contact() #(or) p1.show_all_contact() (or) p2.show_all_contact()

'''
print("==========================")
#searching a particular contact
print(PhoneBook.search_contact("John"))
'''
