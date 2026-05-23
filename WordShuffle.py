import random

level1=("array", "stack", "queue", "cache", "crypt", "logic", "bytes", "float", "token", "macro", "virus",
        "debug", "input", "mouse", "digit", "model", "index", "pivot", "merge", "graph", "nodes", "edges",
        "query", "regex", "scope", "class", "parse", "build", "block", "clock", "drive", "cloud", "frame",
        "event", "error", "shell", "linux", "swift", "codec", "pixel", "audio", "video", "admin", "login",
        "route", "table", "tuple", "image", "email", "print")
level2=("program", "function", "variable", "compiler", "database", "security", "encryption", "algorithm",
        "framework", "interface", "exception", "iteration", "recursion", "protocol", "debugger", "operating",
        "repository", "deployment", "middleware", "container", "virtual", "software", "hardware", "bandwidth",
        "firewall", "filesystem", "datatypes", "parameter", "statement", "expression", "condition", "microchip",
        "environ", "terminal", "keyboard", "network", "endpoint", "localhost", "responsive", "optimizer",
        "processor", "scheduler", "threading", "benchmark", "bootstrap", "debugging", "plaintext", "ciphertext",
        "checksum", "allocator")
level3=("authentication", "authorization", "virtualization", "microprocessor", "multithreading",
        "cybersecurity", "objectoriented", "polymorphism", "encapsulation", "inheritance",
        "cryptography", "infrastructure", "configuration", "serialization", "deserialization",
        "containerization", "orchestration", "hyperparameter", "computational", "responsiveness",
        "synchronization", "interoperability", "telecommunication", "electromagnetic", "implementation",
        "documentation", "visualization", "recommendation", "classification", "regressionmodel",
        "reinforcement", "naturalanguage", "artificialintelligence", "machinelearning", "deeplearning",
        "datamining", "informationtheory", "faulttolerance", "loadbalancing", "distributed", "parallelism",
        "scalability", "maintainability", "observability", "performance", "accessibility",
        "internationalization", "localization", "versioncontrol")
temp=set()
def play_game(level):
    shuffle_word = ''
    word=''
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
    temp_word=random.sample(word,len(word))
    for i in temp_word:
        shuffle_word+=i+' '
    print('(',shuffle_word.upper(),')'+'=?')
    return word
ans=''
score=0
count=0
lvl=''
print('***Welcome to WordShuffle Game***')
print('Say yes to continue (q to quit) :')
while ans.lower()!='q' and lvl!='q':
    user_input=input()
    if 'yes' in user_input.lower():
        print('LEVEL-1 (EASY) LEVEL-2 (MEDIUM) LEVEL-3 (HARD)''\n''Please select the level (1|2|3)')
        while ans.lower()!='q':
            lvl=input()
            if lvl=='1':
                    while ans.lower() != 'q':
                        arrange_word=play_game(1)
                        ans=input()
                        if ans.lower()==arrange_word:
                            print('CORRECT..!')
                            count+=1
                            score+=1
                        else:
                            if ans.lower()!='q':
                                print('INCORRECT..!')
                                count+=1
                                print('Rigth Word is:', arrange_word.upper())
            elif lvl=='2':
                    while ans.lower() != 'q':
                        arrange_word=play_game(2)
                        ans=input()
                        if ans.lower() == arrange_word:
                            print('CORRECT..!')
                            count+=1
                            score+=1
                        else:
                            if ans.lower() != 'q':
                                print('INCORRECT..!')
                                count+=1
                                print('Rigth Word is:', arrange_word.upper())
            elif lvl=='3':
                    while ans.lower() != 'q':
                        arrange_word = play_game(3)
                        ans = input()
                        if ans.lower() == arrange_word:
                            print('CORRECT..!')
                            count += 1
                            score += 1
                        else:
                            if ans.lower() != 'q':
                                print('INCORRECT..!')
                                count += 1
                                print('Rigth Word is:', arrange_word.upper())
            else:
                if lvl.lower()!='q':
                    print('Please enter a number from 1 to 3!')
                else:
                    break
            print('Thank you for playing!')
            print(f'You got {score} words right out of {count} words')
            print(f'Your Score is: {score}')
            if score != 0:
                print('Your Average score is:', str(round((score / count * 100), 2)))
            else:
                print('Your Average score is:' + '0%')
    else:
        if user_input.lower()!='q':
            print('Please enter the valid input...!')
            continue
        else:
            break