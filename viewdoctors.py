import sqlite3
connection = sqlite3.connect("Hospital.db")
result = connection.execute("SELECT * FROM DOCTORS")
for i in result:
    print("doctorname: ",i[0])
    print("qualification: ",i[1])
    print("address: ",i[2])
    print("phoneno: ",i[3])
    print("email: ",i[4])


