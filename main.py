def opt_chocie(ans):
    if ans == 1:
        print("you ordered")
    elif ans == 2:
        print("you got refunded")
    elif ans == 3:
        print("review receved")
    elif ans == 4:
        print("order picked up")
    else:
        print("exist")

print("Wellcome to Food ordering Chatbot")
name = input("What is your name?: ")
age = input("Hello "+ name +" how old are you?: ")
print("How can I help you. ")
answer = int(input("1.Would you like to order? \n2.Would you like a refund? \n3.Would you like to rate you experience \n4.Pick up a mobile order? \n5.Exit \n:"))
opt_chocie(answer)