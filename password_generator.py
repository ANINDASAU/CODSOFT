import string
import random


print("......IS YOUR PASSWORD STRONG ENOUGH......")
print(".........MAKE YOUR PASSWORD STRONG........")
print("........THIS IS PASSWORD_GENERATOR........")

while True:
    if __name__ == "__main__" :
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        u_input = int(input("Enter Password Length: "))

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
    

        random.shuffle(s)
        print("Your Password is: ")
        print("".join(s[0:u_input]))

    try_again = input("Do you want to try again? (yes/no): ").lower()
    if try_again != 'yes':
        break    