import sqlite3
connection = sqlite3.connect("Hospital.db")
getDoctorName = input("Enter the doctorname to be search: ")
result = connection.execute("SELECT * FROM DOCTORS WHERE DOCTORNAME='"+getDoctorName+"'")
for i in result:
    print("doctorname: ",i[0])
    print("qualification: ",i[1])
    print("address: ",i[2])
    print("phoneno: ",i[3])
    print("email: ",i[4])




