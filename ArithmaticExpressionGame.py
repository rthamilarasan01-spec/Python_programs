import random
import re

operators=['+','-','*','/']
def expression(maxi,lenght,level):
    mini=0
    nums=[str(random.randint(mini,maxi)) for _ in range(lenght)]
    while True:
        operands=''
        for i in range(level):
            if len(operands)>=3:
                pass
            else:
                operands+=nums[i]
            operands +=random.choice(operators)
            operands +=nums[i+1]
        if '/0' in operands:
            continue
        else:
            break
    return operands
def play_game(maxi,lenght,level):
    ans = ''
    score = 0
    count = 0
    while 'q' not in ans.lower():
        exp = expression(maxi,lenght,level)
        print('(',exp,')'+'=?')
        while True:
                        ans=input()
                        pattern=r'^-?\d+(\.\d+)?$'
                        if re.match(pattern,ans):
                            if '.' not in str(eval(exp)): #to check weather the answer contains floating point values
                                if str(ans)==str(eval(exp)):
                                    print('Correct!')
                                    score+=1
                                    count+=1
                                    break
                                else:
                                    print('Incorrect!')
                                    count+=1
                                    break
                            else:
                                if exp[0]==exp[2] and exp[1]=='/' and level=='1' or '.0' in str(eval(exp)):
                                    if str(ans)==str(round(eval(exp))):
                                        print('Correct!')
                                        score += 1
                                        count += 1
                                        break
                                if str(ans) == str(round(eval(exp),2)): #to check the rounded value of the user input
                                    print('Correct!')
                                    count += 1
                                    score += 1
                                    break
                                else:
                                    print('Incorrect!')
                                    count+=1
                                    break
                        else:
                            if 'q' in ans.lower():
                                print('Thank you for playing...!')
                                print(f'Your got answered {score} out of {count} questions...')
                                print('Your score is:',score)
                                if count!=0:
                                    print('Your Average is:',str(round(score/count*100,2))+'%')
                                else:
                                    print('Your Average is: 0.0%')
                                break
                            else:
                                print('Please enter a valid answer...')
                                continue
levels=''
print('***Welcome to Arithmatic Calculation Game***')
while 'q' not in levels.lower():
    user_input = input('Say yes to continue?(q to quit): ')
    if 'yes' in user_input.lower():
        print('Level-1(Easy) Level-2(Medium) Level-3(Hard)')
        while 'q' not in levels.lower():
            print('Please select the level(1,2,3,)??: ')
            levels=input()
            if '1' in levels:
                play_game(9,2,1)
                print('Do you want to play again..?"say yes to continue/q to quit": )')
                while True:
                    levels=input()
                    if 'yes' in levels.lower() or 'q' in levels.lower():
                        break
                    else:
                        print('Please enter a valid input...')
                        continue
            elif '2' in levels:
                play_game(20,3,2)
                print('Do you want to play again..?"say yes to continue/q to quit": )')
                while True:
                    levels = input()
                    if 'yes' in levels.lower() or 'q' in levels.lower():
                        break
                    else:
                        print('Please enter a valid input...')
                        continue
            elif '3' in levels:
                play_game(30,4,3)
                print('Do you want to play again..?"say yes to continue/q to quit": )')
                while True:
                    levels = input()
                    if 'yes' in levels.lower() or 'q' in levels.lower():
                        break
                    else:
                        print('Please enter a valid input...')
                        continue
            else:
                if 'q' in levels.lower():
                    break
                else:
                    print('Please enter the number between 1 to 3...')
                    continue
    else:
        if 'q' in user_input.lower():
            break
        else:
            print('Please enter the valid input...!')
            continue