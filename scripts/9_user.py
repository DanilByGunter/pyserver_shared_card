import codecs
import random, string
import uuid
from datetime import datetime
import faker
f = faker.Faker()

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))

txt1 = 'INSERT INTO "user_account"(id, email, registered_at, hashed_password, is_active, is_superuser, is_verified) VALUES'
txt2 = 'INSERT INTO "user"(id, name, weight, height, age) VALUES'
users = ''
n = 120
for i in range(1, n+1):
    user_token = uuid.uuid4()
    txt1 += f''' ('{user_token}','{f.email()}','{datetime.now()}','{randomword(1024)}',True,True,True),'''
    txt2 += f''' ('{user_token}','{randomword(random.randint(4, 24))}',{random.randint(40, 90)},{random.randint(140, 220)},{random.randint(8, 110)}),'''
    users += f'{user_token},'

txt1 = txt1[:len(txt1)-1] + ';'
txt2 = txt2[:len(txt2)-1] + ';'
users = users[:len(users)-1]

with codecs.open("10_user_account.txt", "w", "utf-16") as output:
    output.write(txt1)
with codecs.open("11_user.txt", "w", "utf-16") as output:
    output.write(txt2)
with codecs.open("users.txt", "w", "utf-16") as output:
    output.write(users)