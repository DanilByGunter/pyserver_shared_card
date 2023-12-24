import codecs
import random, string
import uuid
from datetime import datetime
import faker
f = faker.Faker()


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))


check_txt = 'INSERT INTO "check"(id, id_product, id_metric, id_group, id_creator, date_create, description, count, status) VALUES'
history_check_txt = 'INSERT INTO "check"(id, id_product, id_shop, id_metric, id_group, id_creator, id_buyer, id_currency, date_create, date_close, description, count, price, status) VALUES'
target_txt = 'INSERT INTO "target"(id, name, id_category, id_group, id_creator, date_create, description, price_first, status) VALUES'
history_target_txt = 'INSERT INTO "target"(id, name, id_category, id_shop, id_currency, id_group, id_creator, id_buyer, date_create, date_close, description, price_first, price_last, status) VALUES'


group_ass = set()

# вручную
users_groups = {
    '97367365-cdf2-41bf-8017-4576820edc5e': ['323fd391-4272-4220-8c01-c40d404346f5',
                                             '01da8e7f-2ec1-46f2-bd22-430d6fb40848',
                                             '450679cb-bbda-426a-bac0-cadf09ab75fd',
                                             'c0c941a6-dc79-4dbc-b9e5-02d53ffafea9'],
    'cc629279-e987-410a-bc8f-08dbee40b9d1': ['c0c941a6-dc79-4dbc-b9e5-02d53ffafea9',
                                             'ecf18965-70a9-4fb9-ab85-c21a61ab4bfd',
                                             '40fdd27b-6a7c-49ed-b287-4b2ebaaa47a4',
                                             '69e54561-a29f-4476-9501-4279f454bbe7',
                                             '2b09baaa-fe25-4155-922f-3f6b9323700a',
                                             '8a8eec6f-bb77-4ada-9e05-bcd77aa5806d',
                                             '1c162b26-af68-488e-b832-40839668d2cd'],
    '28604f89-bfeb-4932-99c6-4b5a0700d21d': ['e2a52280-ea47-47df-a299-9da8edfac135',
                                             '0599bc1e-7062-4463-ad64-b12fcae74d7f',
                                             'cf403767-eaeb-42f2-b707-6077dae8f592',
                                             '6e6d06b4-1cd0-4a5e-a8bc-90df83e589b9',
                                             'e830001a-2e83-4139-a3ae-d4ad76f94568'],
    '6ef7f0a3-1a25-4d7b-b620-4c2426206c44': ['69e54561-a29f-4476-9501-4279f454bbe7',
                                             'f0082e06-b203-4046-9011-20011710b2f6',
                                             'c9a0c04f-35e1-4c88-bd45-353c3248e275'],
    '188ca743-cd3b-49ad-a871-0f9744477b5c': ['9f392ab9-7003-4995-94bc-e53e962cffc1']
}
    

for group, users in users_groups.items():
    n = random.randint(1, 150)
    for _ in range(n):
        check_txt += f'''('{uuid.uuid4()}', {random.randint(1, 449)}, {random.randint(1, 15)}, 
        '{group}', '{random.choice(users)}', '{datetime.now()}', '{randomword(random.randint(1, 64))}', {random.randint(1, 20)}, True),'''
    n = random.randint(1, 150)
    for _ in range(n):
        history_check_txt += f'''('{uuid.uuid4()}', {random.randint(1, 449)}, {random.randint(1, 27)}, {random.randint(1, 15)}, '{group}', '{random.choice(users)}',
        '{random.choice(users)}', '643', '{datetime.now()}', '{datetime.now()}', 
        '{randomword(random.randint(1, 64))}', {random.randint(1, 20)}, {random.randint(200, 3000)}, False),'''
    n = random.randint(1, 150)
    for _ in range(n):
        target_txt += f'''('{uuid.uuid4()}','{randomword(random.randint(1, 32))}', {random.randint(46, 78)}, '{group}', '{random.choice(users)}', 
        '{datetime.now()}', '{randomword(random.randint(1, 64))}', {random.randint(1, 999999)}, True),'''
    n = random.randint(1, 150)
    for _ in range(n):
        history_target_txt += f'''('{uuid.uuid4()}', '{randomword(random.randint(1, 32))}', {random.randint(46, 78)}, {random.randint(28, 69)}, '643', 
        '{group}', '{random.choice(users)}', '{random.choice(users)}', '{datetime.now()}', '{datetime.now()}', 
        '{randomword(random.randint(1, 64))}', {random.randint(1, 999999)}, {random.randint(1, 999999)}, False),'''
        

check_txt = check_txt[:len(check_txt)-1] + ';'
history_check_txt = history_check_txt[:len(history_check_txt)-1] + ';'
target_txt = target_txt[:len(target_txt)-1] + ';'
history_target_txt = history_target_txt[:len(history_target_txt)-1] + ';'

final = ''

final += check_txt +'\n'
final += history_check_txt +'\n'
final += target_txt +'\n'
final += history_target_txt


with codecs.open("13_check.txt", "w", "utf-16") as output:
    output.write(final)
