import sqlite3
connection = sqlite3.connect("Hospital.db")
getpatientid = input("Enter the patientid to be updated: ")

getPatientName = input("Enter the patientName: ")
getAddress = input("Enter the Address: ")
getPhoneNo = input("Enter the PhoneNo: ")
getEmailId = input("Enter the EmailId: ")
getPincode = input("Enter the Pincode: ")
connection.execute("UPDATE PATIENTS SET PATIENTNAME='"+getPatientName+"',ADDRESS='"+getAddress +"',\
            PHONENO="+getPhoneNo+",EMAILID='"+getEmailId+"',PINCODE="+getPincode+" WHERE PATIENTID="+getpatientid)
connection.commit()
print("updated successsfully")
result = connection.execute("SELECT * FROM PATIENTS")
for i in result:
    print("patientid: ",i[0])
    print("patientname: ",i[1])
    print("address: ",i[2])
    print("phoneno: ",i[3])
    print("email: ",i[4])
    print("pincode: ",i[5])

