import random
database ={
    1234567890 : ["yeti", "baba", "your@gmail.com", "1111", 20000],
    5555555555 : ['girl', 'boy', "mine@gmail.com", "2222", 50000]
    }

def init():
    print("Hello there! Welcome to Prosperity Bank.")
    isValidSelection = False
    while isValidSelection == False:
        selectedOption = int(input("What would you like to do? \n 1. Log In \n 2. Register \n"))
        if(selectedOption == 1):
            isValidSelection = True
            login()
        elif(selectedOption == 2):
            isValidSelection = True
            register()
        else:
            print("Invalid selection. Pleae select 1 or 2")
            
def register():
    first_name = input("Please Enter Your First Name: \n")      
    last_name = input("Enter Your Last Name: \n")  
    email = input("Enter Your Email Address: \n")  
    current_balance = 100000
    password =input("Please Create a Password: \n")  
    accountNumber =  random.randrange(1111111111, 9999999999)
    database[accountNumber] = [first_name, last_name, email, password, current_balance]
    print("You have successfully been registered. Your new account number is %d" %accountNumber)

    
    login()
    
def login():
    print("**************This is the login page******************")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        providedAccNo =int(input("Please provide your account number or press 2 to register as new user\n"))
        if (providedAccNo == 2):
            register()
        for accountNumber, userDetails in database.items():
            if (accountNumber == providedAccNo):
                isPasswordCorrect = False
                while isPasswordCorrect == False:
                    providedPassword = input("Enter your correct password \n")
                    if(userDetails[3] == providedPassword):
                        isPasswordCorrect = True
                        bankOperations(userDetails)
                    print("Wrong password")
        print("Account Not Found")        
                    
def bankOperations(user):
    print("Welcome %s %s." %(user[0], user[1]))
    isSelectingOption = False
    while isSelectingOption == False:
        print("What would you like to do? \n" )
        selectedOption2 = int(input("1. Deposit 2. Withdrawals 3.Complaint 4.Logout 5. Exit \n"))
        if(selectedOption2 == 1):
            deposited = int(input("How much would you like to deposit? \n"))
            user[4]+= deposited
            secondTransaction = int(input("You just deposited %d Naira. And your current balance is %d Naira. Would you like to do anything else? 1. Yes 2. No \n" %(deposited, user[4])))
            if(secondTransaction==1):
                print(selectedOption2)
            elif(secondTransaction==2):
                print("Have a nice day!")
                exit()
            else:
                print("Invalid selection")
        elif(selectedOption2 == 2):
            withdrew = int(input("How much would you like to withdraw? \n")) 
            user[4] -= withdrew
            secondTransaction = int(input("Take your cash %d Naira. Your current balance is %d Naira. Would you like to do anything else? 1. Yes 2. No \n" %(withdrew, user[4])))
            if(secondTransaction==1):
                print(selectedOption2)
            elif(secondTransaction==2):
                print("Have a nice day!")
                exit()
            else:
                print("Invalid selection")
        elif(selectedOption2 == 3):
            complaint = input("Please describe your problem. \n")
            print("Thank you for contacting us. We'd get back to you")
        elif(selectedOption2 == 4):
             print("You have been logged out")
             login()
        elif(selectedOption2 ==5):
             exit()
        else:
            print("Invalid selection. Please select a number between 1 - 5")
            
            
init()