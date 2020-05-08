#%%_00
target = 'stressed'
#ex1
target[::-1]
#ex2
''.join(reversed(list(target)))

#%%_01
t = 'パタトクカシー'
t[::2]

# %%_02
t1 = 'パトカー'
t2 = 'タクシー'
a = ''
for c1, c2 in zip(t1, t2):
    a += c1 + c2 
a

# %%_03
target = "Now I need a drink, alcoholic of course,\
after the heavy lectures involving quantum mechanics."

t_lst = target.split(' ')
pi_lst =[]
for c in t_lst:
    c = c.replace('.', '').replace(',', '')
    pi_lst.append(len(c))

pi_lst


# %%_04
import collections
target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.\
New Nations Might Also Sign Peace Security Clause.\
Arthur King Can.'

num_lst = [1, 5, 6, 7, 8, 9, 15, 16, 19]
tar_lst = target.split(' ')
count = 0
dic = collections.OrderedDict()
for c in tar_lst:
    count += 1
    if count in num_lst:
        dic.update({c[0:1]:count})
    else:
        dic.update({c[0:2]:count})

dic

#%%_05

def ngram(target, num):
    result = []
    for i in range(0, len(target) - num +1):
            result.append(target[i:i + num])
    return result

s = 'I am an NLPer'
w_list = s.split(' ')

ngram(w_list, 2)

# %%_06
t1 = 'paraparaparadise'
t2 = 'paragraph'

X = set(ngram(t1, 2))
Y = set(ngram(t2, 2))

X | Y
X & Y
X - Y 
# %%_07
def change(x, y, z):
    return '{hour}時の{tempature}は{num}'.format(hour=x, tempature=y, num=z)

change(12, '気温', 22.4)

# %%_08
def cipher(target):
    answer = ''
    for c in target:
        if c.isalpha:
            answer += chr(219 - ord(c))
        else:
            answer += c
    return answer

target = 'apple'
cipher(target)

# %%_09
import random
def typoglycemia(s):
    words = s.split(' ')
    new = ''
    answer = []
    for w in words:
        if len(w) > 3:
            new = w[0] + ''.join(random.shuffle(list(w[1:-1]))) + w[-1]
            answer.append(new)
        else:
            answer.append(new)
    return ' '.join(answer)

s = 'I love you'
typoglycemia(s)
# %%
