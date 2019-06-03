import random
def randomDigits():
    lower = 10**(4-1)
    upper = 10**4 - 1
    return random.randint(lower, upper)
print("Your OTP is :")
otpGen= randomDigits()
print(otpGen)
userOTP= int(input("Enter the OTP:"))
if otpGen==userOTP:
    print("1. New Account\n2. Withdraw\n3. Deposit\n4. Balance Enquiry\n5. Demand Draft\n6. Cancel")
    choice=int(input("Enter the number of your choice: "))
    if choice==1:
      print("------New Account---------")
      userName = input("Name: ")
      userAge = input("Age: ")
      userAddr = input("Address: ")
      userPh = input("Contact Number: ")
      userGender = input("Gender: ")
      print("-------------------------------\nA/c Holder Details:\nName: "+userName+"\nAge: "+userAge+"\nAddress: "+userAddr+"\nContact: "+userPh+"\nGender: "+userGender)
    elif choice==2:
      print("------Withdrawl---------")
      userAmt = int(input("Enter the amount you want to withdraw: "))
      if(userAmt <= 100 and userAmt >= 10000):
        print("Limit Exeeded!")
      else:
        print("Here is your Money!")
    elif choice==3:
      print("------Deposit---------")
      depositAmt = int(input("Enter the amount to be deposit: "))
      if depositAmt % 5 == 0:
        print("Money is deposited")
      else:
        print("Enter valid amount")
    elif choice==4:
      print("------Balance Enquiry---------")
      print("Enter choices like:\n1. Deposit amount\n2. Outstanding balance\n3. Minimum Due Amount")
    elif choice==5:
      print("------Demand Draft---------")
      print("Enter the details of the Demand Draft:")
      userBank = input("Name of Bank: ")
      userAcc = input("Name of Account Holder: ")
      bankBranch =input("Name of branch: ")
      totalAmt = int(input("Total Amount: "))
      print ("Demand Draft Details:\nName of Bank: "+userBank+"\nName of Account Holder: "+userAcc+"\nName of branch: "+bankBranch+"\nTotal Amount: "+totalAmt)
    elif choice==6:
      print("-------Exit-------")
      exit()
else:
  print("Invalid Input. Please try again.")