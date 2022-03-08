import sqlite3
connection = sqlite3.connect("Hospital.db")
# connection.execute('''CREATE TABLE DOCTORS(
#                       DOCTORNAME TEXT,
#                       QUALIFICATION TEXT,
#                       ADDRESS TEXT,
#                       PHONENO INTEGER,
#                       EMAILID TEXT
# );''')
print("table has been created successfully")

getDoctorName = input("Enter the doctorName: ")
getQualification = input("Enter the qualification: ")
getAddress = input("Enter the Address: ")
getPhoneNo = input("Enter the PhoneNo: ")
getEmailId = input("Enter the EmailId: ")

connection.execute("INSERT INTO DOCTORS(DOCTORNAME,QUALIFICATION,ADDRESS,PHONENO,EMAILID)\
                   VALUES('"+getDoctorName+"','"+getQualification+"','"+getAddress+"',"+getPhoneNo+",'"+getEmailId+"')")
connection.commit()
connection.close()
print("Inserted successfully")