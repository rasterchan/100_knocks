#%%_10
count = 0
path = 'popular-names.txt'
with open(path) as f:
    for l in f:
        count += 1
print(count)

#%%_10-2
import pandas as pd
path = 'popular-names.txt'
with open(path) as f:
    df = pd.read_table(f, header=None)
    print(len(df))

#%%_11
with open(path) as f:
    for l in f:
        print(l.replace('\t', '　'))

#%%11_2
df = pd.read_table(path, sep='\t', header=None)
df.to_csv('space.txt', sep=' ', header=None, index=False) 

# %%_12
#ex1
import pandas as pd
with open(path) as f:
    df = pd.read_table(f,header=None)
    col1_df = df[0]
    col2_df = df[1]
    col1_df.to_csv('col1.txt', index=None)
    col2_df.to_csv('col2.txt', index=None)

# %%_13
path1 = 'col1.txt'
path2 = 'col2.txt'
import pandas as pd
with open(path1) as f1, open(path2) as f2:
    df1 = pd.read_table(f1,header=None)
    df2 = pd.read_table(f2,header=None)
    df = pd.merge(df1, df2, left_index=True, right_index=True)
    df.to_csv('merge.txt', sep='\t', header = None, index=False,)


# %%_14
import pandas as pd
def head_return(path, n):
    with open(path) as f:
        df = pd.read_table(f)
        return df.head(n)

print(head_return('merge.txt', 5))

# %%_14-2
import sys
import pandas as pd

args = sys.argv
path = args[1]
N = args[2]

def head_return(path, N):
    with open(path) as f:
        df = pd.read_table(f, index_col=0)
        N = int(N)
        return df.head(N)

print(head_return(path, N))

#%%_15　省

#%%_16
import sys
import pandas as pd
import math

args = sys.argv
#N = int(args[1])
N = 3
df = pd.read_table(path, sep='\t', header=None)
nrow = math.ceil(len(df) / N)
for i in range(N):
    df.loc[nrow * i: nrow * (i + 1)].to_csv(f'sep_{i}.txt', sep = '\t', index = False)

#なぜかinvalis syntaxになる
#%%_17
df = pd.read_table(path, sep='\t', header=None)
namelist = df[0].unique()
print(namelist, len(namelist))
# %%_18
print(df.sort_values(2, ascending=False))
# %%_19
df[0].value_counts()

