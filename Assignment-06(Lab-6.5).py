#------Lab-6 Task-01/05 --------
'''Generate Python code to check voting eligibility based on age and citizenship.
Include strong error handling: if the user enters text instead of a number,
floats instead of integers, empty inputs, or invalid citizenship values.
The program must clearly explain the eligibility logic and return meaningful error messages describing the wrong input type'''
def check_voting_eligibility():
    try:
        age_input = input("Enter your age: ").strip()
        if not age_input:
            raise ValueError("Age input cannot be empty.")
        age = int(age_input)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        citizenship = input("Are you a citizen? (yes/no): ").strip().lower()
        if citizenship not in ['yes', 'no']:
            raise ValueError("Citizenship must be 'yes' or 'no'.")
        
        if age >= 18 and citizenship == 'yes':
            return "You are eligible to vote."
        else:
            return "You are not eligible to vote."
    
    except ValueError as ve:
        return f"Input Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
# Example usage:
print(check_voting_eligibility())

#------Lab-6 Task-02/05 --------
'''Generate Python code that counts vowels and consonants in a user-given string using loops only. 
Add detailed error handling for cases where the user enters numbers, special characters, empty strings, or mixed input.
The program should accurately classify only alphabetic characters and clearly display errors when non-string input is entered.'''
def count_vowels_consonants():
    try:
        user_input = input("Enter a string: ").strip()
        if not user_input:
            raise ValueError("Input cannot be empty.")
        
        vowels = 'aeiouAEIOU'
        vowel_count = 0
        consonant_count = 0
        
        for char in user_input:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
            elif char.isdigit() or char in '!@#$%^&*()_+-=[]{}|;:\'",.<>?/`~':
                raise ValueError("Input should not contain numbers or special characters.")
        
        return f"Vowels: {vowel_count}, Consonants: {consonant_count}"
    
    except ValueError as ve:
        return f"Input Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
# Example usage:
print(count_vowels_consonants())

#------Lab-6 Task-03/05 --------
'''Generate a complete Python program for a simple library management system using classes, loops, and conditionals.
 Include strong error handling for invalid menu inputs, numeric/empty entries, and incorrect book names.
 Ensure the program allows adding, listing, and issuing books with meaningful error messages.'''
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book_name):
        if not book_name.strip():
            raise ValueError("Book name cannot be empty.")
        self.books.append(book_name.strip())
        return f"Book '{book_name}' added successfully."
    
    def list_books(self):
        if not self.books:
            return "No books available in the library."
        return "Books in the library:\n" + "\n".join(self.books)
    
    def issue_book(self, book_name):
        if not book_name.strip():
            raise ValueError("Book name cannot be empty.")
        if book_name.strip() in self.books:
            self.books.remove(book_name.strip())
            return f"Book '{book_name}' issued successfully."
        else:
            raise ValueError(f"Book '{book_name}' not found in the library.")
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Issue Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        try:
            if choice == '1':
                book_name = input("Enter the name of the book to add: ")
                print(library.add_book(book_name))
            elif choice == '2':
                print(library.list_books())
            elif choice == '3':
                book_name = input("Enter the name of the book to issue: ")
                print(library.issue_book(book_name))
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                raise ValueError("Invalid menu option. Please choose a valid option (1-4).")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()

#------Lab-6 Task-04/05 --------
'''Generate a Python class for a student attendance system using loops.
 The class must include methods to mark attendance, display attendance, and validate student names.
 Add error handling for empty inputs, numeric inputs, invalid menu options, and missing attendance records.'''
class AttendanceSystem:
    def __init__(self):
        self.attendance = {}
    
    def mark_attendance(self, student_name):
        if not student_name.strip():
            raise ValueError("Student name cannot be empty.")
        if student_name.strip().isdigit():
            raise ValueError("Student name cannot be numeric.")
        
        self.attendance[student_name.strip()] = "Present"
        return f"Attendance marked for {student_name}."
    
    def display_attendance(self):
        if not self.attendance:
            return "No attendance records found."
        return "Attendance Records:\n" + "\n".join(f"{name}: {status}" for name, status in self.attendance.items())
def main():
    attendance_system = AttendanceSystem()
    while True:
        print("\nStudent Attendance System")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        try:
            if choice == '1':
                student_name = input("Enter the student's name to mark attendance: ")
                print(attendance_system.mark_attendance(student_name))
            elif choice == '2':
                print(attendance_system.display_attendance())
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                raise ValueError("Invalid menu option. Please choose a valid option (1-3).")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":    main()

#------Lab-6 Task-05/05 --------
'''Generate Python code for an ATM-style menu using loops and conditionals. 
Include proper error handling for invalid numeric inputs, non-numeric entries, 
empty input, negative amounts, withdrawal greater than balance, and incorrect menu selections.
 Ensure the output is clear and user-friendly.'''
class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        return f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}"
def main():
    atm = ATM()
    while True:
        print("\nATM Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        try:
            if choice == '1':
                amount_input = input("Enter amount to deposit: ").strip()
                if not amount_input:
                    raise ValueError("Amount cannot be empty.")
                amount = float(amount_input)
                print(atm.deposit(amount))
            elif choice == '2':
                amount_input = input("Enter amount to withdraw: ").strip()
                if not amount_input:
                    raise ValueError("Amount cannot be empty.")
                amount = float(amount_input)
                print(atm.withdraw(amount))
            elif choice == '3':
                print(atm.check_balance())
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                raise ValueError("Invalid menu option. Please choose a valid option (1-4).")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
    
