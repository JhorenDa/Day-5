num = []

while True:
    print("1-Add(Naa), 2-Delete(Naa), 3-Add(Wala), 4-Delete(Wala), 5-Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter number: "))
        num.append(number)

    elif choice == "2":
        num.pop(0)

    elif choice == "3":
        number = int(input("Enter number: "))
        num.insert(0, number)

    elif choice == "4":
        num.pop()

    elif choice == "5":
        print("bye.")
        break

    else:
        print("Choose properly")

    print("Current list:", num)
