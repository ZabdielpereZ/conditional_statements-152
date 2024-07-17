# If statements 

# syntax
# if (codition)
#     indents for code block
# 
weather =  'rainy'

assertion = (weather == 'sunny')
print(assertion)

#----------------#

if weather == 'sunny': #if statements are always looking for a true condition/ assertion 
    print("let's have a picnick!")

torch_lit = True

if torch_lit:
    print("My path is clear")

if True:
    print("This will always run because this condition is literally true all the time")

#-----------------------------#

user_input = input("would you like to explore the cave or continue down the spooky path?")

if user_input ==  'cave': 
    print("Ooooooh you just entered a dark cave!!")
elif user_input == 'spooky path':
    print("This path is spooky but you bravely charge forward")
else:
    print("enter valid option!")

# If statements check for a True condition/assertion, if it's True will execute a defined code block 

#--------------------------#

# COMPOUND CONDITIONAL STATEMENTS using 'and' , and 'or' logical operators 

#-- and : requires both conditions are True in order to execute the indented code block 

gold_coins = 10 
silver_coins = 50

if (gold_coins >= 5) and (silver_coins >= 30):
    print("Enough to buy the magic potion!!")


    # or : Requires that at least one condition needs to be True in order for our code block to run 

day = 'monday'

if (day == 'staurdsy') or (day == 'sunday'):
    print("Yaaaaaaaaay its's the weekend!!")

    #print(bool(''))

if day == 'moday' or day == 'tuesday' or day == 'wednesday':
    print("Aww man it's a weekday...")

# ----------------#
 
# Using 'and' and 'or' TOGETHER
 
caffinated = True 
prepared_lvl = 11
confidence = 90 

# How ready am I to teach?

if(caffinated and prepared_lvl > 6) or (confidence > 80):
    print("I'M READYYYYYYY TO TEACH!!!")
else:
    print("Oh no im not ready yet!!!")


dressed = True 
weather = 'sunny'
num_of_friends = 4

if (dressed and num_of_friends > 3) or (weather == 'sunny'):
    print("Lets's go to the beach!!!")

print(dressed and num_of_friends > 3)
print(weather == 'sunny')

#---- using the 'not' operator 

# By incorporating 'not' our if statements can now check for false conditions 

busy = False 

# if not True
if not busy:
    print("Nice! time to relax!")

# If False:
#    run code 

time = 8.30 

if not (time < 7):
    print("I should be awake!")

if not time > 7:
    print("I should be awake!!!!!!!!!")

# there's usually a way to work around having to use 'not' 