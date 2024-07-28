def set1():
    age = int(input("Enter your age: "))

    while not age >= 18:
        print("Sorry, you must be less than 18 years old")
        age = int(input("please reenter your age: "))
    else:
        print(f"Your age is {age}")
        print("you are good to go for pornhub!")


def set2():
    age = int(input("Enter your age: "))
    while age >= 6:
        print("you are too big for this baby roller coaster!")
        age = int(input("please reenter your age: "))
    else:
        print(f"Your age is {age}")
        print("you can ride this roller coaster!")


set1()

