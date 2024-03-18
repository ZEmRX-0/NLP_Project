import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

#use ntlk.download() to get the stop words and lemmas

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english") #could use split() but for conviniace

# Removing Stop Words (words with no emtional impact)
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word) #For standraization or something i just thought its cool
    lemma_words.append(word)

emotion_list = []
with open('en_emotions.txt', 'r',encoding='utf-16') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        
        word, emotion = clear_line.split(':')
        
        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

