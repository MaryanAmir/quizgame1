
play =input('Do you want play ?')
if play == 'yes' :
     print("Great. Let's start")
     score=0
     answer=input('What is 2 + 2?')#question one********************
     if answer == '4': 
        print('correct! youe score is 1')
        score+=1
     else:
        print('incorrect!')
     answer=input('What is 3+ 22?')#question two********************
     if answer == '25': 
        print('correct! youe score is 2')
        score+=1
     else:
        print('incorrect!')
     answer=input('What is 2 * 2?')#question 3********************
     if answer == '4': 
        print('correct! youe score is 3')
        score+=1
     else:
        print('incorrect!')
else:
            quit()

