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
# %%_03
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

# %%
