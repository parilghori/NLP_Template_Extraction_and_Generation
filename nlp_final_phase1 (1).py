# -*- coding: utf-8 -*-
"""nlp final phase1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M4t0q8u1QQ0LoD7OZG_O_3bMq0X0JNUk
"""

import pandas as pd
from pandas.io.json import json_normalize
import re

!python -m spacy download en_core_web_lg
import en_core_web_lg
nlp = en_core_web_lg.load()

import spacy

from google.colab import drive 
drive.mount("/content/gdrive")

!wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-trivia-train.json.gz

!gzip -dk '/content/biencoder-trivia-train.json.gz'

!cp '/content/biencoder-trivia-train.json' '/content/gdrive/MyDrive/NLP'

!pip install ijson
import ijson
import ijson

limit = 0
data = []
with open('/content/gdrive/MyDrive/NLP/biencoder-trivia-train.json', 'r') as f:
    for item in ijson.items(f, "item"):
        if limit == 100:
            break
        data.append(item)
        limit += 1
import pandas as pd
df1 = pd.DataFrame(data, columns=['question'])

df1.head()

templates = []
for index, question in enumerate(df1['question']):
  if index > 100:
    break
  data = nlp(question)
  # print([(X, X.ent_iob_, X.ent_type_) for X in data])
  x = []
  for i, element in enumerate([(X, X.ent_iob_, X.ent_type_) for X in data]):
    if element[2] == '':
      x.append(str(element[0]))
    else:
      x.append('_')
  templates.append([question, re.sub('(_ ){2,}','_ ', ' '.join(x))])

df_template = pd.DataFrame(templates,columns=['Question','Template'])
df_template.head()

df_template.to_csv('/content/gdrive/MyDrive/NLP/ans.tsv',sep='\t', index=False)