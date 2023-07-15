# -*- coding: utf-8 -*-
"""hugging face.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ci63rcMOwJIP1mWTnWP-i4bS-ZfjzKbm
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/gdrive')

data = pd.read_csv("/content/gdrive/MyDrive/AI DATASET.csv", sep=";")

data

!pip install transformers

from transformers import pipeline

import pandas as pd

pipe = pipeline(task='text2text-generation', model='facebook/nllb-200-distilled-600M')

!pip install transformers
!pip install sentencepiece

!pip install transformers
!pip install sentencepiece

from transformers import MarianMTModel, MarianTokenizer
import transformers
import sentencepiece

print("Transformers version:", transformers.__version__)
print("SentencePiece version:", sentencepiece.__version__)

model_name = 'Helsinki-NLP/opus-mt-zh-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text):
    # Tokenize the input text
    batch = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")

    # Move the batch to the GPU if available
    batch = batch.to(model.device)

    # Perform the translation and get the model's output
    translated = model.generate(**batch)

    # Decode the output from model tokens to text
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

    return tgt_text[0]

# Translate a Chinese text to English
text_zh = "(重要通知)112學年學士班宿舍中籤學生選填床位方式說明"

print("Translated:", translate(text_zh))