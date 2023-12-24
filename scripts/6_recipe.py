import codecs
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))

txt = 'INSERT INTO recipe(id, name, name_en, description, portion, calories) VALUES'
n = 100
for i in range(1, n+1): 
    txt += f''' ({i},'Рецепт{i}','Recipe{i}','{randomword(random.randint(1, 128))}',{random.randint(1, 12)}, 0),'''

txt = txt[:len(txt)-1] + ';'

with codecs.open("6_recipe.txt", "w", "utf-16") as output:
    output.write(txt)
