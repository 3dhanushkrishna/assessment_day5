import sqlite3
connection = sqlite3.connect("Hospital.db")
getpatientid = input("Enter the patientid to be deleted: ")
connection.execute("DELETE FROM PATIENTS WHERE PATIENTID="+getpatientid)
connection.commit()
print("deleted successfully")
result = connection.execute("SELECT * FROM PATIENTS")
for i in result:
    print("patientid: ",i[0])
    print("patientname: ",i[1])
    print("address: ",i[2])
    print("phoneno: ",i[3])
    print("email: ",i[4])
    print("pincode: ",i[5])


