#%%_00
w = "stressed"
w[::-1]

# %%_02
#パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から
#交互に連結して文字列「パタトクカシーー」を得よ．

w1 = "パトカー"
w2 = "タクシー"
result = ""

for (a, b) in zip(w1, w2):
    result += a + b
print(result)
# %%_03
'''Now I need a drink,
 alcoholic of course, after the heavy lectures involving 
 quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）
 文字数を先頭から出現順に並べたリストを作成せよ．
'''
txt = "Now I need a drink,\
 alcoholic of course, after the heavy lectures involving\
 quantum mechanics."
txt = txt.replace(',', '').replace('.', '')
w_lst = txt.split(' ')
pi = list()
for i in w_lst:
    pi += str(len(i))
pi
# %%_03*
txt2 = "Now I need a drink,\
 alcoholic of course, after the heavy lectures involving\
 quantum mechanics."
w_lst2 = txt2.split(' ')
result = []

for word in w_lst2:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    result.append(count)

print(result)

# %%_04
"""Hi He Lied Because Boron Could Not Oxidize Fluorine.\
New Nations Might Also Sign Peace Security Clause. \
Arthur King Can."という文を単語に分解し，\
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，\
それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置
(先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．"""

target = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
New Nations Might Also Sign Peace Security Clause. \
Arthur King Can."
target_list = target.split(" ")
len(target_list)
one_word = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element = {}
for i in range(len(target_list)):
    if i in one_word:
        for m in range(len(one_word)):
            word = target_list[m]
            element[i] = word[0:1:]
    else:
        word = target_list[i]
        element[i] = word[0:2:]

element

# %%_04*
# coding: utf-8
num_first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
result = {}

words = target.split(' ')
for (num, word) in enumerate(words, 1):
    if num in num_first_only:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num

print(result)
# %%_07
"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""
def ans(x, y, z):
    print('%d時の%sは%f' % (x, y, z))
    
ans(12, '気温', 22.4)

# %%_07*
def format_string(x, y, z):
    return '{hour}時の{target}は{value}'.format(hour=x, target=y, value=z)


# テスト
x = 12
y = '気温'
z = 22.4
print(format_string(x, y, z))