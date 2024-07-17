# Nested if statements

# We can have nested if's, or if statements inside of an if statement

#Activity of the day 

weather = 'sunny'
friends = 5

if weather == 'sunny': # outter conditions
    # inner if's
    if friends <= 6:
        print("Lets play volleyball!!")
    elif friends == 5:
        print("Let's play frisbee!")
    else:
        if friends == 1:
            print("I think ill play golf all by my blonesome...")
        elif friends < 5:
            print("The", friends , "of us should play golf")
else:
    print("Let's go to the movies!")