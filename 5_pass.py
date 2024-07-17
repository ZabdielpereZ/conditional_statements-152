# Pass statement is a place holder keyword, or temporary standin for a codeblock 

feeling = 'decent'

if feeling == 'sick':
    pass
elif feeling == 'decent':
    pass
elif feeling == 'good':
    pass
else:
    print("Wow, I'm feeling great, let's go running!")

#------------------------#

user_input = input("where do you want to go?")

if user_input == 'cave':
    pass # expand on options for cave exploration
elif user_input == 'left fork':
    pass # Options for what happens when you choose to go left
elif user_input == 'lake':
    pass # what happens at the lake?
else:
    print("choose a valid option")