import mysql.connector as sql
import sys

import choose_faculty as choose_fac
import insert
import modify
import view
import feeChecking

conn = ''
c1 = ''


        

def mysql_connect():
    global conn
    global c1
    conn=sql.connect(host='localhost',user='root',passwd='root',database='hostel_management')
    conn.autocommit=True
    if conn.is_connected():
        print('connected to my_sql succesfully')
    else:
        print('not connected')

    c1=conn.cursor()
        
def main():
    choose = "y"
    while(choose=="y"):
        mysql_connect()
        print("-----------------------------WELCOME TO  HOSTEL MANAGEMENT--------------------------------------")

        print("     1.ADMISSION FORM")

        print("     2.FEE CHECKING")

        print("     3.MODIFY DATA")
        print("     4.VIEW DATA")

        print("     5.EXIT")
        choice=int(input('ENTER YOUR CHOICE: '))
        if choice==1:
            insert.insert(conn,c1) 
        elif choice==2:
            feeChecking.feeChecking(c1)
        elif choice == 3:
            modify.modify(c1,conn)
        elif choice == 4:
            view.view(c1)
        elif choice == 5:
            print("\nThank you for visiting!!!")
            break;

        choose = input("Do you want to continue y/n?")
        if choose != "y":
            print("\nThank you for visiting!!!")
main()