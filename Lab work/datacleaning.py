
import re

sentence = "Nory was a Catholic because her mother was a Catholic, and Nory's mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been.” Six repetitions in this sentence!"

text_tx = re.search('olic',sentence)
recognise = re.sub('olic' , '-',sentence)
print(text_tx)
print(recognise)
spl = re.split('olic',sentence)
print(spl)

"""HTML tag removal"""

import re
tag_html = re.compile('<.?/?[a-zA-Z]*[^>]*>')

tag = "<title>Title of the document</title><h1>This is a heading</h1><p>This is a paragraph.</p>"
remove_tag = re.sub(tag_html,' ', tag)
print(remove_tag)

"""HTML Parser

"""

from bs4 import BeautifulSoup

html_code = """
<head>
  <title>This is a title of the document</title>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>

"""
soup = BeautifulSoup(html_code, 'lxml')
ttl = soup.title.string
print(ttl)

head = soup.h1.string
print(head)

"""Emoji removal"""

import re

text = "I woke up feeling great today! 😁 I couldn’t help but smile like a grinning face \n😀 when I saw the beautiful sunrise. Later, I met a friend who had the grinning face with big eyes 😃,\n and we shared some laughs. We both felt like the beaming face with smiling eyes 😁\n when we talked about our plans for the weekend. After that, a funny video made me burst into tears of joy 😂! \nWe even shared our favorite moments, and I looked at my friend with heart-eyes 😍,\n feeling grateful for their friendship. It’s amazing how a thinking face 🤔\n can lead to such happy moments!\n"
def remove_emoji(text):
  #Convert emojis in string we use unicode
  emojis = re.compile("[ '\U0001F600 ', '\U0001F382 ', '\U00002764 ', '\U0001F602','\U0001F60D','\U0001F914','\U0001F603','\U0001F601',' \U0001F604 ']")
  remove_cont = re.sub(emojis,' ',text)
  return remove_cont

main = remove_emoji(text)
print("Original text\n"+ text)

print("Without Emojis\n"+main)

pip install pyspellchecker



!pip install textblob

from textblob import TextBlob

text = " I amm stuyddnt from dkte collleg"

def correct(text):
  obj = TextBlob(text)
  word = obj.correct()
  return str(word)

main = correct(text)
print("Original text : " + text)
print("Corrected text : " + main)