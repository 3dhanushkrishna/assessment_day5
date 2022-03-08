import sqlite3
connection = sqlite3.connect("Hospital.db")
result = connection.execute("SELECT * FROM PATIENTS")
for i in result:
    print("patientid: ",i[0])
    print("patientname: ",i[1])
    print("address: ",i[2])
    print("phoneno: ",i[3])
    print("email: ",i[4])
    print("pincode: ",i[5])
