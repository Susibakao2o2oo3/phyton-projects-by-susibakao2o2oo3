import time
thetrue = "true"
password = input("password:")
combination = 0
while thetrue == "true":
    combination += 1
    print(combination)
    if combination == int(password):
        print("correct " + str(combination))
        thetrue = "false"
    
    
