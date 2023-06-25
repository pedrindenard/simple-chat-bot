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
Add you additional data inside "data.txt" file like example below

````
Chatbot creation
The process of creating a chatbot follows a pattern similar to the development of a web page or a mobile app. It can be divided into Design, Building, Analytics and Maintenance.

Design
The chatbot design is the process that defines the interaction between the user and the chatbot.The chatbot designer will define the chatbot personality, the questions that will be asked to the users, and the overall interaction.It can be viewed as a subset of the conversational design. In order to speed up this process, designers can use dedicated chatbot design tools, that allow for immediate preview, team collaboration and video export.An important part of the chatbot design is also centered around user testing. User testing can be performed following the same principles that guide the user testing of graphical interfaces.

Building
The process of building a chatbot can be divided into two main tasks: understanding the user's intent and producing the correct answer. The first task involves understanding the user input. In order to properly understand a user input in a free text form, a Natural Language Processing Engine can be used.The second task may involve different approaches depending on the type of the response that the chatbot will generate.
```

## How to run
```
python chatbot.py
```