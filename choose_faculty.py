def choose_faculty():
    print("AVAILABLE DEPARTMENTS AS FOLLOWS")
    print("1.COMPUTER")
    print("2.BIO")
    print("3.TECH")
    print("4.PHYSICS")
    print("5.ECO")
    print("6.ENG")
    choice = int(input("Please choose the faculty.\n"))
    if (choice == 1):
        return "COMPUTER"
    elif(choice ==2):
        return "BIO"
    elif(choice ==3):
        return "TECH"
    elif(choice ==4):
        return "PHYSICS"
    elif(choice ==5):
        return "ECO"
    elif(choice==6):
        return "ENG"
    else:
        print("Please choose the above given option.")