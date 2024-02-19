import contractions
import re
from string import punctuation

def clean_text(text):
    #Remove contractions 
    text = contractions.fix(text)
    # Make lower case
    text = text.lower()
    # remove punctuation
    text = re.sub("[%s]"% re.escape(punctuation), "", text) 
    
    #remove numbers
    text = re.sub(r"\w*\d\w*", "", text)
    #remove stop words
    stopword= [stopword.strip() for stopword in open("./8 feb/data/stopwords_eng.txt", "r")]
    return " ".join([word for word in text.split() if word not in stopword])
    
    



text = " I read this book for the first time in 1987, and it's still one of my favorites!"

cleaned_text = clean_text(text)
print(cleaned_text)