

def view(c1):
    roll_no=int(input("Enter your roll number: "))
    mysql="select*from hostel_management where roll_no={}".format(roll_no)
    c1.execute(mysql)
    data=c1.fetchall()
    print("\nHere is your requested data\n")
    print("Roll_no:",data[0][0])
    print("Name:",data[0][1])
    print("Address:",data[0][2])           
    print("Room_no:",data[0][3])
    print("Dept:",data[0][4])
    print("Fees:",data[0][5])           
    print("Bal:",data[0][6])
    