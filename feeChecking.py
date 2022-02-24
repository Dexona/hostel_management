import choose_faculty as choose_fac
def feeChecking(c1):
    try:
        department=choose_fac.choose_faculty()
        mysql="select*from hostel_management where dept='{}'".format(department)
        c1.execute(mysql)
        data=c1.fetchall()
        print("your fees is:",data[0][5])
    except:
        print("\nIt seems that you are not registered to this faculty, please try again.")