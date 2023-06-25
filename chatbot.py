import random
import string
import warnings
import nltk
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.stem import WordNetLemmatizer

from phrases import *

warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)  # For downloading packages

# Uncomment the following only the first time
# nltk.download('punkt')
# nltk.download('wordnet')

# List of archives names
archives = os.listdir('data/')

# List to storage data from each file
sent_tokens = []
word_tokens = []

# Loop to process all archives
for archive in archives:
    with open('data/' + archive, 'r', encoding='utf8', errors='ignore') as fin:
        raw = fin.read().lower()

        # Tokens
        sent_tokens += nltk.sent_tokenize(raw)  # Converts to list of sentences
        word_tokens += nltk.word_tokenize(raw)  # Converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):

    robo_response = ''
    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]

    flat = vals.flatten()
    flat.sort()

    req_tfidf = flat[-2]

    if (req_tfidf == 0):

        robo_response = robo_response + UNKNOWN_RESPONSE
        return robo_response
    
    else:

        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag = True

print(GREETING_INITIAL_RESPONSE)

while (flag == True):

    user_response = input()
    user_response = user_response.lower()

    if (user_response == INPUT_THANKS_L or user_response == INPUT_THANK_YOU_L):

        flag = False
        print(FINISH_RESPONSE)

    else:

        if (greeting(user_response) != None):

            print("BOT: " + greeting(user_response))

        else:

            print("BOT: ", end = "")
            print(response(user_response))
            sent_tokens.remove(user_response)