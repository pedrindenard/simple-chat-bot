# Building a Simple Chatbot from Scratch in Python (using NLTK)

### Installation of NLTK
```
pip install nltk
```

### Installing required packages
After NLTK has been downloaded, install required packages

```
import nltk

from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)
nltk.download('punkt') 
nltk.download('wordnet') 
```

### How to add data
Add you additional data, inside package "data/", add files .txt to tokenizer and get results when user asks for more different data

````
data/data1.txt
data/data2.txt
data/data3.txt
data/data4.txt
data/data5.txt
........
```

## How to run
```
python chatbot.py
```