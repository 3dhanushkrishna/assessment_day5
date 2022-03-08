import sqlite3
connection = sqlite3.connect("Hospital.db")
getphoneno = input("Enter the phoneno to be updated: ")

getDoctorName = input("Enter the new doctorName: ")
getQualification = input("Enter the new Qualification: ")
getAddress = input("Enter the new Address: ")
getPhoneNo = input("Enter the new PhoneNo: ")
getEmailId = input("Enter the new EmailId: ")
connection.execute("UPDATE DOCTORS SET DOCTORNAME='"+getDoctorName+"',QUALIFICATION='"+getQualification+"',ADDRESS='"+getAddress +"',\
            PHONENO="+getPhoneNo+",EMAILID='"+getEmailId+"' WHERE PHONENO="+getphoneno)
connection.commit()
print("updated successsfully")
result = connection.execute("SELECT * FROM DOCTORS")
for i in result:
    print("doctorname: ",i[0])
    print("qualification: ",i[1])
    print("address: ",i[2])
    print("phoneno: ",i[3])
    print("email: ",i[4])



