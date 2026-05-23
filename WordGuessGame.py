import random
import json

with open('word_json.json', 'r') as f:
    dictionary = json.load(f)

levels = []

for value in dictionary.values():
    levels.append(tuple(value))

level1 = levels[0]
level2 = levels[1]
level3 = levels[2]

temp=set()
def play_game(level):
    word=''
    temp_dict={}
    while True:
        if level==1:
            word=random.choice(level1)
            if len(temp)==len(level1):
                temp.clear()
        elif level==2:
            word=random.choice(level2)
            if len(temp)==len(level2):
                temp.clear()
        elif level==3:
            word=random.choice(level3)
            if len(temp)==len(level3):
                temp.clear()
        if word not in temp:
            temp.add(word)
            break
        else:
            continue
    dummy_word=['_' for _ in range(len(word))]
    if len(word)%2==0:
        no=int(len(word)/2)
    else:
        no=round(len(word)/2)+1
    for i in range(no):
        while True:
            ind = random.randint(0,len(word) - 1)
            if str(ind) not in temp_dict:
                temp_dict.update({str(ind):word[ind]})
                break
            else:
                 continue
    for k,v in temp_dict.items():
        dummy_word[int(k)]=v
    display_word=''
    for i in dummy_word:
        display_word+=i+' '
    print('(',display_word.upper(),')'+'=?')
    return word
score=0
count=0
ans=''
lvl=''
print('***Welcome to WordGuess Game***''\n''Say yes to continue (q to quit)')
while ans.lower()!='q' and lvl!='q':
    user_input=input()
    if user_input.lower()=='yes':
        print("LEVEL-1(EASY) LEVEL-2(MEDIUM) LEVEL-3(HARD)")
        print('Please select the level...!(1,2,3)')
        while ans.lower()!='q':
            lvl=input()
            if lvl=='1':
                while ans.lower()!='q':
                    word_guess=play_game(1)
                    ans=input()
                    if ans.lower()==word_guess:
                        print('Correct..!')
                        count+=1
                        score+=1
                    else:
                        if ans.lower()!='q':
                            print('Incorrect..')
                            count+=1
                            print('Rigth Word is:',word_guess.upper())
            elif lvl=='2':
                while ans.lower()!='q':
                    word_guess=play_game(2)
                    ans=input()
                    if ans.lower()==word_guess:
                        print('Correct..!')
                        count+=1
                        score+=1
                    else:
                        if ans.lower()!='q':
                            print('Incorrect..')
                            count+=1
                            print('Rigth Word is:', word_guess.upper())
            elif lvl=='3':
                while ans.lower()!='q':
                    word_guess=play_game(3)
                    ans=input()
                    if ans.lower()==word_guess:
                        print('Correct..!')
                        count+=1
                        score+=1
                    else:
                        if ans.lower()!='q':
                            print('Incorrect..')
                            count+=1
                            print('Rigth Word is:', word_guess.upper())
            else:
                if lvl=='q':
                    break
                else:
                    print('Please enter number between 1 to 3.')
                    continue
            print('Thank you for playing!')
            print(f'You got {score} words correct in {count} words.')
            print('Your Score is:',score)
            if score!=0:
                print('Your Average Score is:',str(round(score/count*100,2))+'%')
            else:
                print('Your Average Score is:'+'0%')
    else:
        if user_input.lower()=='q':
            break
        else:
            print('Please enter a valid input')
            continue
