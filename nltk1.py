import nltk 
import pandas as pd

train = pd.read_csv('F:/Data_Scientist/Textmining/toxiccomments/data/train.csv').fillna(' ')
test = pd.read_csv('F:/Data_Scientist/Textmining/toxiccomments/data/test.csv').fillna(' ')


train_text = train['comment_text']
test_text = test['comment_text']
all_text = pd.concat([train_text, test_text])

FreqDist(all_text)
