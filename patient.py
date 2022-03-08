import sqlite3
connection = sqlite3.connect("Hospital.db")
# connection.execute('''CREATE TABLE PATIENTS(
#                       PATIENTID INTEGER PRIMARY KEY AUTOINCREMENT,
#                       PATIENTNAME TEXT,
#                       ADDRESS TEXT,
#                       PHONENO INTEGER,
#                       EMAILID TEXT,
#                       PINCODE INTEGER
# );''')
print("table has been created successfully")

getPatientName = input("Enter the patientName: ")
getAddress = input("Enter the Address: ")
getPhoneNo = input("Enter the PhoneNo: ")
getEmailId = input("Enter the EmailId: ")
getPincode = input("Enter the Pincode: ")
connection.execute("INSERT INTO PATIENTS(PATIENTNAME,ADDRESS,PHONENO,EMAILID,PINCODE)\
                   VALUES('"+getPatientName+"','"+getAddress+"',"+getPhoneNo+",'"+getEmailId+"',"+getPincode+")")
connection.commit()
connection.close()
print("Inserted successfully")