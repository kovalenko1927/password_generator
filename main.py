import random


def get_password():

    while True:

        length = input("How long should the password be? (print 'q' to exit) >>> ")
        description = input("What platform is the password for? >>> ")
        save_password = input("Do you want to save the password to a file? (y/n) >>> ")

        if length != "q" and save_password == "y":
            numbers = "1234567890"
            letters = "abcdefghijklmnopqrstuvwxyz"
            symbols = "!@#$%^&*()/"
            all_symbols = numbers + letters + letters.upper() + symbols
            random_list = random.sample(all_symbols, int(length))
            password = "".join(random_list)
            with open("passwords.txt", 'a') as f:
                f.write(f"{description.upper()} --- {password}\n")
            print(f"Here your random password >>> {password}")

        else:
            print("Bye-Bye")
            break


if __name__ == "__main__":
    get_password()





