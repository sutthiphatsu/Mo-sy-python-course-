"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
class name_info():
    def name():
        name = input("Enter Your Name is:")
        age =  int(input("Enter Your age is:"))
        phone_number = input("Enter Your phonenumber is:")
        user_phone_number = False
        for i in name:
            if i.isalpha() or i.isspace():
                user_name = True
            else:
                user_name = False
        check_age = False

        if 18 <= age <=65:
            check_age = True
        user_phone_number = False
        if phone_number.isdigit() and len(phone_number) == 10:
            user_phone_number = True

        if user_name == False:
            print("Validation Results:")
            print("Name: Valid (contains only letters and spaces)")

        if user_name == True:
            print("=== PERSONAL INFORMATION VALIDATOR ===")
            print(f"Name:{name}")

        if check_age == True:
            print(f"Age:{age}")

        if check_age == False:
            print(f"Age: Valid ({age})")

        if user_phone_number == False:
            print("Phone: Valid (10-digit number)")

        if user_phone_number == True:
            print(f"Phone:+91-{phone_number}")
name_info.name()