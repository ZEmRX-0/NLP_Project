import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import ISRIStemmer
from nltk.tokenize import word_tokenize
import arabic_reshaper
from bidi.algorithm import get_display
import sys

stop_words_arabic = set(stopwords.words('arabic'))

text = open('read.txt', encoding='utf-8').read()

tokenized_words = word_tokenize(text)

cleaned_text = [word.strip(string.punctuation) for word in tokenized_words]

final_words = [word for word in cleaned_text if word not in stop_words_arabic]

stemmer = ISRIStemmer()

stemmed_words = [stemmer.stem(word) for word in final_words]

# problems with encoding cant figure it out HELP!!!!!!!!!!



'''
emotion_list = []
with open('ar_emotions.txt', 'r', encoding='utf-16') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        
        word, emotion = clear_line.split(':')
        
        if word in stemmed_words:
            emotion_list.append(emotion)

print(emotion_list)

emotion_counter = Counter(emotion_list)
print(emotion_counter)

fig, ax1 = plt.subplots()
ax1.bar(emotion_counter.keys(), emotion_counter.values())

plt.xticks(rotation=90)
for label in ax1.get_xticklabels():
    label.set_fontproperties('Arial')  
    label.set_fontsize(10) 
    label.set_text(get_display(arabic_reshaper.reshape(label.get_text())))

plt.tight_layout()
plt.savefig('graph.png')
plt.show()
'''
