
def game_quiz(question):
    score = 0 
    for x in question:
        print('\n'+ x['ask'])
        for a in x['options']:
            print(a)
        replay=input('Enter you answer (A/B/C) : ').upper()

        while replay not in ['A','B','C']:
            replay =input('Invalid input please try again . ').upper()

        if replay == x['answer']:
            print('✅ Correct!')
            score += 1

        else:
            print(f'❌ Wrong! the right answer is {x["answer"]}')
        print(f'your score is {score}')
question=[{'ask':'What is the fastest thing in the world?',
            'options':['A.Sound','B.Light','C.Money'],
            'answer':'C'} ,
           { 'ask':' 2, 4, 8, 16, ... ?',
            'options':['A.31','B.32','C.33'],
            'answer':'B'
           },
            { 'ask':' If you try to succeed in anything, which have you done??',
            'options':['A.succeed','B.The biggest succeed','C.there is no option'],
            'answer':'B'
           }]

game_quiz(question)