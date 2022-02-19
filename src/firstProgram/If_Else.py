def add(var1, var2):
    return var1 + var2


def subtract(var1, var2):
    return var1 - var2


def main():
    start = True
    while start:
        command = input("Enter Add / Subtract : ")

        if command == "Add":
            print(add(int(input("Enter number 1: ")), int(input("Enter number 2: "))))
        elif command == "Subtract":
            print(subtract(int(input("Enter number 1: ")), int(input("Enter number 2: "))))
        else:
            start = False
            print("BYE BYE...!!!")


main()
