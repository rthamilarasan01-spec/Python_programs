import json
import random

start_char='<'
end_char='>'
start_index=-1
temp_title_list=set()
with open("Story_json.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)
title_list=list(json_data.keys())
print(type(title_list))
print('Welcome to Story Creator')
print('நீங்கள் கதையை உருவாக்க விரும்புகிறீர்களா? ஆம் என்றால் \n(yes) Enter செய்யவும் இல்லையென்றால் (no) Enter செய்யவும் :')
user_input=''
word_input=''
while word_input.lower() !='no':
    words = set()
    user_input = input()
    if 'yes' in user_input.lower():
        while True:
            random_title=random.choice(title_list)
            if random_title not in temp_title_list:
                temp_title_list.add(random_title)
                break
            else:
                if len(temp_title_list)==len(title_list):
                    temp_title_list=set()
                continue
        story=json_data[random_title]
        for i,char in enumerate(story):
            if char == start_char:
                start_index = i
            if char == end_char and start_index !=-1:
                word=story[start_index:i+1]
                words.add(word)
                start_index=-1
        print()
        print("கதைக்கு தேவையான வார்த்தைகளை உள்ளிடவும்...")
        for i in words:
            word_input=input(f'Enter the value for {i}: ')
            story=story.replace(i, word_input)
            if word_input.lower() =='no':
                print('நன்றி மீண்டும் வருக...!')
                break
        if word_input.lower()!='no':
            print()
            print(random_title)
            print()
            print(story.replace('\\',''))
            print()
            print('மீண்டும் தொடர விரும்பினால் (yes) அல்லது (no) Enter செய்யவும்')
    else:
        if 'no' not in user_input.lower():
            print('Please enter "yes" or "no"')
            print('தயவு செய்து (yes) அல்லது (no) Enter செய்யவும்')
        else:
            print('நன்றி மீண்டும் வருக...!')
            break