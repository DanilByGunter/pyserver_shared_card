from datetime import datetime
import random
import codecs
from enum import Enum, unique
import uuid

@unique
class Role(Enum):
    CREATOR = "creator"
    ADMIN = "admin"
    USER = "user"

txt = 'INSERT INTO "group_user_association"(id_user, id_group, status, date_invite) VALUES'

user_file = open('users.txt','r', encoding='utf-16')
group_file = open('groups.txt','r', encoding='utf-16')

users = str(*user_file)
group = str(*group_file)

group_ass = set()

users_list, group_list = [], []
for pos in range(0, len(group), 37):
    group_list.append(group[pos:pos+36])
for pos in range(0, len(users), 37):
    users_list.append(users[pos:pos+36])

for group in group_list:
    numb = random.randint(1, 100)
    status = True
    for pos in range(1, len(users_list)):
        if pos%numb == 0:
            txt += f''' ('{users_list[pos]}','{group}','{'CREATOR' if status else 'USER'}','{datetime.now()}'),'''
            status = False
            group_ass.add(group)

groups_txt = ''
for group in group_ass:
    tmp = str(group)
    groups_txt += tmp
    groups_txt += ','
groups_txt = groups_txt[:len(groups_txt)-1]
txt = txt[:len(txt)-1]

with codecs.open("12_group_ass.txt", "w", "utf-16") as output:
    output.write(txt)
with codecs.open("group_ass_token.txt", "w", "utf-16") as output:
    output.write(groups_txt)
# print(users)
# group_user_association