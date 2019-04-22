import random
otpGen=random.randint(1,20)
firstName, lastName = input("Enter your First Name:"), input("Enter your Last Name:")
print ("Hello " + firstName + " " + lastName + " " +"Your OTP:")
print(otpGen)
for i in range(0,3):
    otpUser=int(input("Enter the OTP:"))
    if otpUser<=20:
        if otpUser==otpGen:
            print("Success!")
            break
        elif i==2:
            print("Ran out of Tries!") 
        else:
            print("Incorrect otp!")
            userResponse=input("Want to continue? (Y/N): ")              
            if userResponse=="N" or userResponse=="n":
                print("Program will now exit.")
                break
    else:
        print ("Try Again! Wrong Input")
        break