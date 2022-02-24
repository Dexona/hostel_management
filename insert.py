import choose_faculty as choose_fac

def insert(conn,c1):

    v_roll=input("ENTER YOUR ROLL NUMBER: ")
    v_name=input("ENTER YOUR NAME: ")
    v_add=input("ENTER YOUR ADDRESS: ")
    v_room_no=input("ENTER YOUR ROOM NUMBER: ")
    v_dept=choose_fac.choose_faculty()
    v_fees=input("ENTER YOUR FEES: ")
    v_bal=input("ENTER YOUR BALANCE: ")

    abc=("insert into hostel_management values ("+v_roll+",'"+v_name+"','"+v_add+"',"+v_room_no+",'"+v_dept+"',"+v_fees+","+v_bal+")")
    c1.execute(abc)
    conn.commit()
    print("\nData of "+v_name+" inserted successfully.")
    