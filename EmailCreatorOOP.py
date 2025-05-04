class EmailCreator:
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def create_email(self):
        first_initial = self.first_name[0].lower()
        # Make the surname lowercase
        surname_lower = self.surname.lower()
        email = f"{first_initial}.{surname_lower}@dundeeandangus.ac.uk"
        return email

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

email_creator = EmailCreator(first_name, surname)

email_address = email_creator.create_email()
print("Your email address is:", email_address)