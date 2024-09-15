def Science_quiz():
    print("Hi there, my name is bot. Whats yours")
    response = input("Enter name :")
    
    if response == "":
        print("No name? Rude....\n Goodbye")
        print(exit())
    else:
        print("Its a pleasure to meet you",response)
    
    print("")
    
    print("I will ask you a series of 3 Science questions\nAre you up for it?")
    
    response2 = input("Yes/No :")
    if response2 == "yes":
        print("Splendid,Lets begin!")
        print("")
    if response2 == "no":
        print("Thats okay, Goodbye")
        print(exit())
    else:
        print("Please retry by re-running the code and picking one of the options given above")
    print("please pick a number from the given options")
    print("")
    
    print("Who came up with the first law of motion?")
    
    print("1.Albert Einstein\n2.Isaac Newton\n3.Nicola Tesla\n4.Naruto")
    options = ["1.Albert Einstein","2.Isaac Newton","3.Nicola Tesla","4.Naruto"]
    options[0]
    options[1]
    options[2]
    options[3]

    answer1 = input("Enter number :")
    if answer1 == "2":
        print("Correct \n+2 points")
        point1 = int(2)
    else:
        print("Incorrect\n+0 points")
        point1 = int(0)
    print("Your current score is", point1)
    print("")
    
    print("Who demonstrated the connection between electricity and lightning?")
    
    print("1.Benjamin Flanklin\n2.Thales of Miletus\n3.James Maxwell")
    options2 = ["1.Benjamin Flanklin","2.Thales of Miletus","3.James Maxwell","4.Goku"]
    options2[0]
    options2[1]
    options2[2]
    options2[3]
    answer2 = input("Enter answer :")
    if answer2 == "2":
        print("correct!\n +2 points")
        point2 = int(2)
    else:
        print("incorrect\n+0 points")
        point2 = int(0)
    print("Your current score is", point1 + point2)
    print("")
    
    if point1 + point2 == 4:
        print("Youre doing great so far, keep it up")
    elif point1 + point2 == 2:
        print("You can still improve")
    else:
        print("You need to study more buddy")
    print("")
    
    print("Who was the first man on the moon?")
    
    print("1.David Goggins\n2.Tim Dunk\n3.Neil Armstrong\n4.Neil Kurosaki")
    
    options3 = ["1.David Goggins","2.Tim Dunk","3.Neil Armstrong","4.Neil Kurosaki"]
    options3[0]
    options3[1]
    options3[2]
    options3[3]
    answer3 = input("Enter answer :")
    if answer3 == "3":
        print("Correct!\n +2 points")
        point3 = int(2)
    else:
        print("incorrect!\n +0 points")
        point3 = int(0)
    
    print("your current score is", point3 + point2 + point1)
    print("")
    
    total_score = point1 + point2 + point3
    print("your total score is :", total_score)
    print("")
    if total_score > 4:
        print("Great job, you sure know your stuff")
    else:
        print("Try again, atleast you completed the quiz right?")

    print("How was the quiz on a scale of 1 to 10?")
    answer = input("Insert number :")
    if answer > "5":
        print("Thank you, Enjoy the rest of your day")
        print(exit())
    else:
        print("Really?\n Alright I'll try to improve")
        print(exit())
    #remember to add the whole points system


Science_quiz()