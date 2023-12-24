import codecs
import random, string
import uuid
from datetime import datetime

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))

txt1 = 'INSERT INTO "group"(id, name, creation_date) VALUES'
txt2 = 'INSERT INTO "group_token"(id, token, date) VALUES'
groups = ''

n = 50
for i in range(1, n+1):
    group_id = uuid.uuid4()
    if i%4 == 0:
        txt1 += f''' ('{group_id}','','{datetime.now()}'),'''
    else:
        txt1 += f''' ('{group_id}','group{i}','{datetime.now()}'),'''
    txt2 += f''' ('{group_id}','{randomword(12)}','{datetime.now()}'),'''
    groups += f'{group_id},'

txt1 = txt1[:len(txt1)-1] + ';'
txt2 = txt2[:len(txt2)-1] + ';'
groups = groups[:len(groups)-1]

with codecs.open("8_group.txt", "w", "utf-16") as output:
    output.write(txt1)
with codecs.open("9_group_token.txt", "w", "utf-16") as output:
    output.write(txt2)
with codecs.open("groups.txt", "w", "utf-16") as output:
    output.write(groups)