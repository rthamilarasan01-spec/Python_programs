import json

title_start_index = -1
title_start='('
title_end=')'
story_start_index = -1
story_start='['
story_end=']'
title_list=[]
story_list=[]
story_dictionary={}
with open('Story.txt', 'r', encoding='utf-8') as file:
    content = file.read()
for i,char in enumerate(content):
    if char == title_start:
        title_start_index = i
    if char == title_end and title_start_index != -1:
        word=content[title_start_index:i+1]
        title_list.append(word)
    if char == story_start:
        story_start_index = i
    if char == story_end and story_start_index != -1:
        word=content[story_start_index:i+1]
        story_list.append(word)
for i in range(len(title_list)-1):
    title_list[i]=title_list[i].replace('(','')
    title_list[i] = title_list[i].replace(')', '')
for i in range(len(story_list)-1):
    story_list[i]=story_list[i].replace('[','')
    story_list[i] = story_list[i].replace(']', '')
story_dictionary=dict(zip(title_list,story_list))

with open('Story_json.json', 'w', encoding='utf-8') as file:
    json.dump(story_dictionary, file, ensure_ascii=False, indent=4)
print('Done')
