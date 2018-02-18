import os
import nltk 
import pandas as pd

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


train = pd.read_csv('./toxiccomments/data/train.csv').fillna(' ')
test = pd.read_csv('./toxiccomments/data/test.csv').fillna(' ')


train_text = train['comment_text']
test_text = test['comment_text']
all_text = pd.concat([train_text, test_text])


